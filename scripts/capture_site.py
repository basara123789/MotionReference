"""Interactive Playwright capture helper; NOT an automatic site scraper.

Install: pip install playwright && python -m playwright install chromium
Run: python scripts/capture_site.py
Select an animation manually in the browser, press Enter to record snapshot.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://motion-reference.takayustudio.jp/"
OUTPUT = Path("captures")
OUTPUT.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    print("Choose a reference in the browser. Enter captures, q quits.")
    count = 0
    while input("Capture [Enter/q]: ").strip().lower() != "q":
        count += 1
        output = OUTPUT / f"reference-{count:03d}"
        page.screenshot(path=str(output.with_suffix(".png")))
        data = page.evaluate("""() => ({
            title: document.title,
            url: location.href,
            visibleText: document.body.innerText.slice(0, 12000),
            animations: document.getAnimations().slice(0,100).map(a => ({
                playState: a.playState,
                animationName: a.animationName || null,
                timing: a.effect ? a.effect.getTiming() : null,
                keyframes: a.effect && a.effect.getKeyframes ? a.effect.getKeyframes() : null
            }))
        })""")
        data["captured_at_utc"] = datetime.now(timezone.utc).isoformat()
        data["review_status"] = "unverified_dom_snapshot"
        output.with_suffix(".json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8"
        )
        print("Saved", output.with_suffix(".json"))
    browser.close()
