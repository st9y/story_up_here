import streamlit as st
import asyncio
import sys
import os
import nest_asyncio
from playwright.async_api import async_playwright

# 1. إعدادات التوافق مع أنظمة التشغيل والسحابة
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
nest_asyncio.apply()

# 2. إعداد واجهة المستخدم
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
st.write("شاهد وحمل ستوريات إنستقرام للحسابات العامة بهوية مجهولة")

# 3. دالة جلب البيانات (المحرك الأساسي)
async def get_insta_stories(username):
    async with async_playwright() as p:
        try:
            # تشغيل المتصفح، وفي حال فشله على السحابة يتم تثبيته تلقائياً
            try:
                browser = await p.chromium.launch(headless=True)
            except Exception:
                st.info("جاري تهيئة محرك المتصفح للمرة الأولى... قد يستغرق هذا دقيقة واحدة.")
                os.system("playwright install chromium")
                browser = await p.chromium.launch(headless=True)
            
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            # التوجه للموقع الوسيط للجلب
            await page.goto(f"https://www.save-free.com/ar/insta-stories-viewer/", timeout=60000)
            await page.fill('input#username', username)
            await page.click('button#btn-view')
            
            # انتظار ظهور النتائج لمدة 15 ثانية كحد أقصى
            await page.wait_for_selector('.story-item', timeout=15000)
            
            stories_data = []
            items = await page.query_selector_all('.story-item')
            
            for item in items:
                img = await item.query_selector('img')
                video = await item.query_selector('video source')
                
                if video:
                    url = await video.get_attribute('src')
                    stories_data.append({'type': 'video', 'url': url})
                elif img:
                    url = await img.get_attribute('src')
                    stories_data.append({'type': 'image', 'url': url})
            
            await browser.close()
            return stories_data
            
        except Exception as e:
            if 'browser' in locals(): await browser.close()
            return None

# 4. منطق التشغيل في الواجهة
username_input = st.text_input("أدخل اسم المستخدم (بدون @):", placeholder="f.xzon")

if st.button("عرض الستوريات الآن"):
    if username_input:
        with st.spinner("🚀 جاري استخراج الستوريات..."):
            # تشغيل العملية بشكل غير متزامن
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            stories = loop.run_until_complete(get_insta_stories(username_input))
            
            if stories:
                st.success(f"✅ تم العثور على {len(stories)} ستوري")
                cols = st.columns(2)
                for idx, item in enumerate(stories):
                    with cols[idx % 2]:
                        if item['type'] == 'video':
                            st.video(item['url'])
                        else:
                            st.image(item['url'], use_container_width=True)
                        
                        # رابط تحميل مباشر
                        st.markdown(f"[📥 تحميل مباشرة]({item['url']})")
            else:
                st.error("❌ لم يتم العثور على ستوريات. تأكد أن الحساب عام (Public) وليس خاصاً.")
    else:
        st.warning("⚠️ يرجى كتابة اسم المستخدم أولاً.")