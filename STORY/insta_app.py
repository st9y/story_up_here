import streamlit as st
import requests

# إعدادات الصفحة
st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")

st.title("📸 Insta Chick Pro")
st.write("عرض ستوريات إنستقرام للحسابات العامة بمجهولية تامة")

def get_stories_stable(username):
    # استخدام محرك جلب سريع يتجاوز حظر السيرفرات
    api_url = f"https://storiesig.info/api/ig/stories/{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get('result', [])
        return None
    except:
        return None

user_input = st.text_input("أدخل اسم المستخدم (مثال: 5n_21am):")

if st.button("عرض الستوريات الآن"):
    if user_input:
        clean_user = user_input.replace('@', '').strip()
        with st.spinner("🚀 جاري جلب البيانات..."):
            stories = get_stories_stable(clean_user)
            
            if stories and len(stories) > 0:
                st.success(f"✅ تم العثور على {len(stories)} عنصر")
                for url in stories:
                    if ".mp4" in url or "video" in url:
                        st.video(url)
                    else:
                        st.image(url)
            else:
                st.error("❌ تعذر الجلب حالياً. قد يكون الحساب خاصاً أو إنستقرام يفرض حظراً مؤقتاً.")
    else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم أولاً.")