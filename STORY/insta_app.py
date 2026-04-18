import streamlit as st

st.set_page_config(page_title="Insta Chick Pro - Gold", page_icon="🔥")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #f9ce34, #ee2a7b, #6228d7);
        color: white; border-radius: 15px; font-weight: bold; padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Insta Chick Pro: Gold Edition")
username = st.text_input("👤 أدخل اسم المستخدم (بدون @):")

is_human = st.checkbox("✅ أنا لست ريبورت (تأكيد الهوية)")

if st.button("🚀 جلب الستوريات الآن"):
    if not is_human:
        st.error("⚠️ يرجى تأكيد أنك لست ريبورت!")
    elif username:
        user_clean = username.replace('@', '').strip()
        # توجيه مباشر يتخطى حظر السيرفرات تماماً
        target = f"https://saveig.app/en/instagram-story-viewer/{user_clean}"
        st.success(f"جاري فتح المحرك العالمي للحساب: {user_clean}")
        st.markdown(f'<meta http-equiv="refresh" content="1;URL=\'{target}\'">', unsafe_allow_html=True)
    else:
        st.warning("⚠️ أدخل اسم المستخدم أولاً.")