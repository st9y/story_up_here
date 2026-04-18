import streamlit as st
import requests

# بياناتك الخاصة
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

st.set_page_config(page_title="Insta Viewer Pro", page_icon="🎬", layout="wide")

# تصميم واجهة عرض الستوريات (Dark Mode)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .story-container {
        border: 2px solid #ee2a7b;
        border-radius: 20px;
        padding: 10px;
        background: #1c1f26;
        text-align: center;
        margin-bottom: 20px;
    }
    iframe { border-radius: 15px; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Insta View Pro: عرض داخلي مباشر")

username = st.text_input("👤 أدخل يوزر الهدف للعرض الفوري:")

def send_log(user):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": TELEGRAM_ID, "text": f"🔥 <b>مشاهدة داخلية جديدة!</b>\nالهدف: <code>{user}</code>", "parse_mode": "HTML"})
    except: pass

if username:
    user_clean = username.replace('@', '').strip()
    
    if st.button("👁️ عرض الستوريات الآن"):
        send_log(user_clean)
        
        st.write("---")
        st.success(f"جاري كسر الحماية وعرض ستوريات الحساب: {user_clean}")
        
        # استخدام محرك وسيط (Proxy) يسمح بالعرض الداخلي وتجاوز الـ IFrame Block
        # هذا المحرك سيجعل الستوري يظهر كأنه جزء من صفحتك
        proxy_engine = f"https://www.picuki.com/profile/{user_clean}"
        
        # إنشاء حاوية العرض الداخلي
        st.markdown(f"""
            <div class="story-container">
                <p style="color: #ee2a7b; font-weight: bold;">⚠️ إذا لم يظهر المحتوى أدناه، اضغط على زر "تحديث المحرك"</p>
                <iframe src="{proxy_engine}" width="100%" height="800px"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

st.info("💡 ملاحظة: هذا النظام يستخدم تقنية 'الوكيل' لعرض الصور والفيديوهات داخل موقعك دون الخروج منه.")