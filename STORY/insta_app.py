import streamlit as st
import requests

# إعداد واجهة المستخدم
st.set_page_config(page_title="Insta Chick Pro", page_icon="📸", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #e1306c;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Insta Chick Pro")
st.write("عرض ستوريات إنستقرام للحسابات العامة بسرعة واستقرار")

def get_stories(username):
    # استخدام API وسيط قوي لتجاوز حظر سيرفرات Streamlit
    api_url = f"https://api.proxiesapi.com/instagram/stories?username={username}"
    # ملاحظة: هذا API تجريبي، في حال توقفه سنستخدم المحرك الاحتياطي أدناه
    backup_url = f"https://storiesig.info/api/ig/stories/{username}"
    
    try:
        response = requests.get(backup_url, timeout=15)
        if response.status_code == 200:
            return response.json().get('result', [])
        return None
    except:
        return None

user_input = st.text_input("أدخل اسم المستخدم (بدون @):", placeholder="f.xzon")

if st.button("عرض الستوريات الآن"):
    if user_input:
        with st.spinner("🚀 جاري جلب البيانات من إنستقرام..."):
            stories = get_stories(user_input)
            
            if stories and isinstance(stories, list):
                st.success(f"✅ تم العثور على {len(stories)} عنصر")
                cols = st.columns(2)
                for idx, url in enumerate(stories):
                    with cols[idx % 2]:
                        if ".mp4" in url or "video" in url:
                            st.video(url)
                        else:
                            st.image(url, use_container_width=True)
            else:
                st.error("❌ تعذر الجلب. تأكد أن الحساب عام (Public) ولديه ستوري نشط حالياً.")
    else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم.")