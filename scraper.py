from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException

chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://wix-visual-data.appspot.com/app/widget?cacheKiller=1602828679412&commonConfig=%7B%22brand%22%3A%22wix%22%2C%22consentPolicy%22%3A%7B%22essential%22%3Atrue%2C%22functional%22%3Atrue%2C%22analytics%22%3Atrue%2C%22advertising%22%3Atrue%2C%22dataToThirdParty%22%3Atrue%7D%2C%22consentPolicyHeader%22%3A%7B%7D%2C%22bsi%22%3A%22434d3e95-3f41-47d6-ade7-61b6a52817e3%7C3%22%7D&compId=comp-jc25pxgc&deviceType=desktop&height=2097&instance=dJ9bc5BStS5NtJKhpeglpFXDvDxNB0ZArpgBmNzy95k.eyJpbnN0YW5jZUlkIjoiMDRmMjJjY2MtODRhNC00ZmZkLWE0MDEtMDkwMzBjYzlhZjExIiwiYXBwRGVmSWQiOiIxMzQxMzlmMy1mMmEwLTJjMmMtNjkzYy1lZDIyMTY1Y2ZkODQiLCJtZXRhU2l0ZUlkIjoiZDRkYzNlOGEtZDk4YS00NWI4LWJkMTUtNDU0YjExMGNhNjU1Iiwic2lnbkRhdGUiOiIyMDIwLTEwLTE2VDA2OjExOjE4LjMzMloiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImM2Y2M5OGRiLTJkYzMtNGUxYS1iMzU3LThmZmE1YjNlYmY3ZiIsImJpVG9rZW4iOiJkMDJlMTI0Ni01ZDJlLTBhNDUtMTkxNC00YzQ4MWRjNTA5NDQiLCJzaXRlT3duZXJJZCI6ImYwMTQzMjUyLWIxZmYtNDIzZS1iZTRjLWNkYmE0ZjRmYTJiMyJ9&locale=en&pageId=dbj4j&siteRevision=397&viewMode=site&viewerCompId=comp-jc25pxgc&vsi=7e8f31e5-64da-4823-b855-57c8d5b9a6c4&width=946")

driver.implicitly_wait(10)

el = driver.find_element_by_tag_name("tbody").get_attribute('innerHTML')

soup = BeautifulSoup(el)
for row in soup.select('tr'):
    print(row)

driver.quit()