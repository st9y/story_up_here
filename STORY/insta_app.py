import streamlit as st
import asyncio
import os
import nest_asyncio
from playwright.async_api import async_playwright

nest_asyncio.apply()

st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")

st.title("📸 Insta Chick Pro")
st.write("شاهد ستوريات الحسابات العامة بمجهولية تامة")

async def get_stories(username):
    async with async_playwright() as p:
        # محاولة تشغيل المتصفح مع إعدادات تجاوز الحماية
        try:
            browser = await p.chromium.launch(headless=True)
        except Exception:
            os.system("playwright install chromium")
            browser = await p.chromium.launch(headless=True)
            
        # إعداد المتصفح ليتصرف كأنه مستخدم حقيقي
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 720}
        )
        page = await context.new_page()
        
        try:
            # استخدام موقع بديل أكثر استقراراً للجلب
            await page.goto(f"https://snapinsta.app/ar/instagram-stories-viewer", timeout=60000)
            await page.fill('input#url', username)
            await page.click('button[type="submit"]')
            
            # انتظار معالجة الطلب (15 ثانية)
            await asyncio.sleep(15) 
            
            # جلب روابط الصور والفيديوهات
            results = []
            elements = await page.query_selector_all('a[download]')
            for el in elements:
                href = await el.get_attribute('href')
                if href and "http" in href:
                    results.append(href)
            
            await browser.close()
            return list(set(results)) # إزالة الروابط المكررة
        except Exception as e:
            await browser.close()
            return f"Error: {e}"

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("عرض الستوريات"):
    if user_input:
        with st.spinner("جاري جلب الستوريات... قد يستغرق الأمر ثوانٍ قليلة"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            stories = loop.run_until_complete(get_stories(user_input))
            
            if isinstance(stories, list) and len(stories) > 0:
                st.success(f"تم العثور على {len(stories)} عنصر")
                for link in stories:
                    if ".mp4" in link or "video" in link:
                        st.video(link)
                    else:
                        st.image(link)
            else:
                st.error("فشل الجلب. جرب اسماً آخر أو تأكد أن الحساب لديه ستوري نشط الآن.")