import streamlit as st
import zxcvbn
import secrets
import string

# 1. App Header
st.title("🛡️ Password Strength Analyzer")
st.write("Enter a password to evaluate its security.")

# 2. User Input
password = st.text_input("Enter Password", type="password")

# 3. Logic
if password:
    # Analyze the password
    result = zxcvbn.zxcvbn(password)
    score = result['score'] # 0 to 4
    
    # Visual Feedback
    ratings = ["🔴 Very Weak", "🟠 Weak", "🟡 Fair", "🟢 Strong", "🌟 Very Strong"]
    st.subheader(f"Rating: {ratings[score]}")
    st.progress((score + 1) * 20)

    # Show Warnings
    if result['feedback']['warning']:
        st.warning(f"⚠️ {result['feedback']['warning']}")
    
    # Show Suggestions
    if result['feedback']['suggestions']:
        st.info("💡 Tips to improve:")
        for s in result['feedback']['suggestions']:
            st.write(f"- {s}")

    # 4. Strong Alternative Generator
    if score < 3:
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        suggestion = ''.join(secrets.choice(chars) for i in range(16))
        st.success(f"Suggested Secure Password: `{suggestion}`")
        