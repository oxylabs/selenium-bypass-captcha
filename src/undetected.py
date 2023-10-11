import undetected_chromedriver as webdriver

browser = webdriver.Chrome(headless=True, use_subprocess=True)
browser.get("https://sandbox.oxylabs.io/products")
browser.save_screenshot("screenshot.png")
