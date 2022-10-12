from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

URL = "URL"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    "User-Agent": "USER-AGENT"

}

links = []

response = requests.get(url=URL, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

prices = [x.text.split("+")[0].split("/mo")[0] for x in soup.find_all(name="div", class_="list-card-price")]

for x in soup.find_all(name="div", class_="list-card-top"):
    url = x.find('a')['href']
    links.append(url)
    if url.split("/")[0] != "https:":
        print(url.split("/")[0])
        y = links.index(url)
        r = f"https://www.zillow.com{url}"
        links.insert(y, r)

addresses = [x.text for x in soup.find_all(name="address")]

chrome_driver_path = r"CHROME_DRIVER_PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("GOOGLE_FORMS_LINK")
driver.maximize_window()
time.sleep(3)

y = 0
for x in addresses:
        inputs = driver.find_elements_by_css_selector(".freebirdFormviewerViewItemList div input")
        input_ad = inputs[0]
        input_pri = inputs[1]
        input_lin = inputs[2]

        input_ad.click()
        input_ad.send_keys(f"{x}")

        input_pri.click()
        input_pri.send_keys(f"{prices[y]}")

        input_lin.click()
        input_lin.send_keys(f"{links[y]}")

        submit_button= driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        submit_button.click()


        response_send=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        response_send.click()

        y += 1
        time.sleep(3)









