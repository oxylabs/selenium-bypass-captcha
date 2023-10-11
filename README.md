#How to Bypass CAPTCHA With Selenium & Python

In this tutorial, you’ll learn how to handle CAPTCHA tests in Selenium
and Python using
[<u>undetected-chromedriver</u>](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
and [<u>Oxylabs’ Web
Unblocker</u>](https://oxylabs.io/products/web-unblocker). See the
[<u>full blog post</u>](https://oxylabs.io/blog/selenium-bypass-captcha)
for more details and tips.

## Bypass CAPTCHA with Selenium and Python

The first step is to install Python if you haven't installed it already.
You can download it from the [<u>official
website</u>](https://python.org/download). Download the latest version
or a version greater than 3.6; otherwise, undetected-chromedriver won’t
work properly.

### **Step 1 - Install dependencies**

Install the `undetected-chromedriver` and `requests` module. You can use the
`pip` command given below:

```bash
pip install undetected-chromedriver requests
```

### **Step 2 - Import libraries**

Now that you’ve installed undetected-chromedriver, you can import it as
shown below:

```python
import undetected_chromedriver as webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")

browser = webdriver.Chrome(options=chrome_options)
```

Notice, you’ve also created a `browser` instance. This will open a
Chrome window in the background in `headless` mode.

### **Step 3 - Navigate to webpage**

Use the `browser` instance to navigate to your target website. For
this tutorial, let’s use
[<u>https://sandbox.oxylabs.io/products</u>](https://sandbox.oxylabs.io/products)
as the target.

```python
browser.get("https://sandbox.oxylabs.io/products")
```

### **Step 4 - Take a screenshot**

Take a screenshot to verify the page is loaded properly without showing
any CAPTCHA or bot protection screen. You can use the
`save_screenshot` method of Selenium.

```python
browser.save_screenshot("screenshot.png")
```

Your screenshot might vary slightly due to screen size, but it’ll look
similar to the one given below:



The page has loaded properly without showing any CAPTCHA and the
undetected-chromedriver has rendered the Javascript files.

## **Bypass CAPTCHA with Web Unblocker**

To perform large-scale web scraping while bypassing CAPTCHA, you’ll need
a strong tool. [<u>Web
Unblocker</u>](https://oxylabs.io/products/web-unblocker), an AI–powered
proxy solution for bypassing IP blocks and CAPTCHAs, will automatically
rotate proxies for you, so you don’t have to worry about manually
managing a list of proxies for your bots.

### **Step 1 - Import libraries**

Let’s use the `requests` module to set up Web Unblocker.

```python
import requests
```

### **Step 2 - Get Web Unblocker credentials** 

Create an account to get the Web Unblocker credentials. Within a few
clicks, you can sign up and get a **1-week free trial** to develop and
thoroughly test the solution.

### **Step 3 - Prepare Web Unblocker** 

Web Unblocker’s host and port are `unblock.oxylabs.io` and `60000`
respectively. Additionally, don’t forget to replace the `USERNAME` and
`PASSWORD` with the correct credentials.

```python
proxy = 'http://{}:{}@unblock.oxylabs.io:60000'.format("USERNAME", "PASSWORD")

proxies = {
    'http': proxy,
    'https': proxy
}
```

If you get any authentication-related errors in the later steps, don’t
forget to check the Web Unblocker response codes
[<u>here</u>](https://developers.oxylabs.io/advanced-proxy-solutions/web-unblocker/response-codes).

### **Step 4 - Fetch content**

Now, you can use the `proxies` dict you created with the `get`
method of the `requests` module. Web Unblocker also requires you to
pass an extra parameter, `verify=False`, to the get method.

```python
page = "https://sandbox.oxylabs.io/products"
response = requests.get(page, proxies=proxies, verify=False)

print(response.status_code)
content = response.content
```

You should see the status code `200` if everything works as expected.
The content of the page will be stored in the `content` object, which
you can process later with HTML Parser libraries such as [<u>Beautiful
Soup</u>](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) or
parse using the [<u>Custom
Parser</u>](https://developers.oxylabs.io/scraper-apis/custom-parser).
Web Unblocker also renders JavaScript for you, so you can use this
method for dynamic websites as well.
