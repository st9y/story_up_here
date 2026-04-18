import streamlit as st
import requests

# إعداد واجهة التطبيق بشكل احترافي
st.set_page_config(page_title="Insta Chick Pro", page_icon="📸", layout="centered")

# إضافة نمط CSS مخصص ليشبه المواقع العالمية
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d);
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
    }
    .status-box {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Insta Chick Pro")
st.info("الأداة الآن تعمل عبر محرك جلب خارجي لتجاوز حظر الريبورت 🤖")

def fetch_stories_advanced(username):
    # استخدام محرك جلب خارجي (API) يحاكي المواقع التي أرفقتها في صورك
    api_url = f"https://storiesig.info/api/ig/stories/{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://storiesig.info/"
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=20)
        if response.status_code == 200:
            return response.json().get('result', [])
        return "ERROR_BLOCK"
    except:
        return None

# مدخل اسم المستخدم
user_input = st.text_input("أدخل اسم المستخدم (بدون @):", placeholder="مثال: an.or.8")

# محاكاة "أنا لست ريبورت" البسيطة (Checkbox) لزيادة الأمان
not_bot = st.checkbox("أنا لست برنامج ريبورت (I'm not a robot)")

if st.button("تحميل الستوريات الآن"):
    if not not_bot:
        st.warning("⚠️ يرجى تأكيد أنك لست ريبورت أولاً.")
    elif user_input:
        username = user_input.replace('@', '').strip()
        with st.spinner(f"🔍 جاري الاتصال بخوادم الجلب للحساب {username}..."):
            stories = fetch_stories_advanced(username)
            
            if stories == "ERROR_BLOCK":
                st.error("❌ تم كشف محاولة الجلب من قبل إنستقرام. جرب استخدام VPN أو انتظر 5 دقائق.")
            elif stories and len(stories) > 0:
                st.success(f"✅ تم العثور على {len(stories)} ستوري نشط")
                
                # عرض الستوريات في شبكة منظمة
                for url in stories:
                    with st.container():
                        st.markdown("---")
                        if ".mp4" in url or "video" in url:
                            st.video(url)
                        else:
                            st.image(url, use_container_width=True)
                        st.download_button("💾 تحميل الملف", data=requests.get(url).content, file_name=f"{username}_story.jpg", mime="image/jpeg")
            else:
                st.error("❌ لم يتم العثور على ستوريات. تأكد أن الحساب عام (Public) وليس خاصاً.")
    else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم.")