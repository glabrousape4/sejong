import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1900, "height": 400},
            device_scale_factor=3
        )
        url = "file://C:/Users/glabr/.cloudflared/sites/sejong/detail-compare-render.html"
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(1500)
        # Capture only the compare-table-wrap (no body padding)
        wrap = page.locator('.compare-table-wrap')
        out = "C:/Users/glabr/.cloudflared/sites/sejong/detail-compare-render.png"
        await wrap.screenshot(path=out)
        await browser.close()

asyncio.run(main())
