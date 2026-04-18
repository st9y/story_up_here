import streamlit as st
import instaloader

# إعداد واجهة المستخدم
st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")
st.title("📸 Insta Chick Pro")
st.write("عرض ستوريات الحسابات العامة بسرعة واستقرار")

def get_stories_final(username):
    L = instaloader.Instaloader()
    try:
        # جلب البروفايل
        profile = instaloader.Profile.from_username(L.context, username)
        
        # التحقق إذا كان الحساب عاماً
        if profile.is_private:
            return "private"
        
        stories_links = []
        # محاولة جلب الستوريات العامة
        for story in L.get_stories(userids=[profile.userid]):
            for item in story.get_items():
                if item.is_video:
                    stories_links.append({"type": "video", "url": item.video_url})
                else:
                    stories_links.append({"type": "image", "url": item.url})
        return stories_links
    except Exception as e:
        return str(e)

user_input = st.text_input("أدخل اسم المستخدم (بدون @):")

if st.button("عرض الستوريات الآن"):
    if user_input:
        with st.spinner("🚀 جاري الاتصال بخوادم إنستقرام..."):
            results = get_stories_final(user_input)
            
            if results == "private":
                st.error("❌ هذا الحساب خاص (Private). لا يمكن عرض ستورياته.")
            elif isinstance(results, list):
                if len(results) > 0:
                    st.success(f"✅ تم العثور على {len(results)} ستوري")
                    for item in results:
                        if item['type'] == 'video':
                            st.video(item['url'])
                        else:
                            st.image(item['url'])
                else:
                    st.warning("⚠️ الحساب لا يوجد به ستوريات نشطة حالياً.")
            else:
                st.error(f"❌ حدث خطأ أثناء الجلب: {results}")
    else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم.")