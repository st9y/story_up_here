import streamlit as st
import requests

# بياناتك الخاصة التي طلبت دمجها
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

st.set_page_config(page_title="Insta Radar Pro", page_icon="📡", layout="centered")

# تصميم الهكرز المحترف (Neon Green & Black)
st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #39ff14; }
    .stTextInput input { border: 2px solid #39ff14 !important; background-color: #000 !important; color: #39ff14 !important; }
    .stButton>button {
        width: 100%; background: #39ff14; color: black; font-weight: bold;
        border-radius: 5px; padding: 15px; border: none; font-size: 20px;
    }
    .stButton>button:hover { background: #2bff00; box-shadow: 0 0 20px #39ff14; }
    </style>
    """, unsafe_allow_html=True)

st.title("📡 Insta Radar: Neural Bypass")
st.write("---")

def send_to_telegram(user_target):
    try:
        msg = f"🎯 <b>عملية جلب جديدة</b>\n👤 الهدف: <code>{user_target}</code>\n🚀 تم اختراق حظر الـ IP بنجاح."
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": TELEGRAM_ID, "text": msg, "parse_mode": "HTML"})
    except:
        pass

# واجهة الاستخدام
target_user = st.text_input("📡 أدخل يوزر الهدف للاختراق:")

col1, col2 = st.columns(2)

if target_user:
    u = target_user.replace('@', '').strip()
    
    with col1:
        if st.button("🔥 جلب سريع"):
            send_to_telegram(u)
            # استراتيجية التوجيه المشفر (تغيير جذري للرابط)
            link = f"https://www.google.com/url?q=https://saveig.app/en/instagram-story-viewer/{u}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'">', unsafe_allow_html=True)

    with col2:
        if st.button("🛰️ جلب عميق"):
            send_to_telegram(u)
            link = f"https://www.google.com/url?q=https://igsaved.com/story-viewer/{u}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'">', unsafe_allow_html=True)

st.markdown("---")
st.warning("⚠️ تم تفعيل بروتوكول التخفي. كل عملياتك الآن تمر عبر نفق مشفر إلى تليجرام.")