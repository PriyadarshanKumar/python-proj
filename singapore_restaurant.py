import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# installing chrome webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())

sg_restaurants_url = 'https://food.grab.com/sg/en/'
driver.get(sg_restaurants_url)
enter_location_singapore = driver.find_element(By.ID, "location-input").send_keys("Singapore General Hospital - 1 Hospital Drive, Singapore, 169608")
button = driver.find_element(By.CLASS_NAME, "ant-btn")
button.click()
time.sleep(2.4)
count = 0

# Will click "Load More" maximum 10 times , or until "Load More" element is exhausted.
while count < 2:
    try:
        time.sleep(7)
        button = driver.find_element(By.CLASS_NAME, "ant-btn")
        button.click()
        count = count + 1
    except:
        print("Number of pages scraped: ",count)
        count = 50

name_elements = driver.find_elements(By.XPATH, "//div[@class ='ant-layout']" and "//div[@class = 'ant-row-flex RestaurantListRow___1SbZY']" and "//div[@class ='ant-col-24 RestaurantListCol___1FZ8V  ant-col-md-12 ant-col-lg-6']" and "//h6[@class = 'name___2epcT']")

# Removing first 10 restaurant from page because the page has an initial section on
# promoted restaurants that we don't need and these are dropped.
name_elements = name_elements[10:]
name_list = []
for name_element in name_elements:
    name_list.append(name_element.text)

url_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/sg/en/restaurant')]")
url_elements_list = []
for url_element in url_elements:
    url_elements_list.append(url_element.get_attribute("href"))
# Removing first 10 url from page because the page has an initial section on
# promoted restaurants's url that we don't need and these are dropped.
url_elements_list = url_elements_list[10:]

## Printing Restaurant_NAME Restaurant_URL
for i in range(len(name_list)):
    print(name_list[i] + "  " + url_elements_list[i])

print("\n\nGetting the Lat Long for each restaurant.......\n\n")
print("RESTAURANT_NAME                 LATITUDE        LONGITUDE")
# Looping through each restaurant page to get latitude and longitude.
# Needed to use driver.get(url), since the requests.get(url) was blocked and not able to retrieve anything.
for i in range(len(name_list)):
    try:
        url = url_elements_list[i]
        driver.get(url)
        jsoninfo = driver.find_element(By.XPATH, '//*[@id="__NEXT_DATA__"]')
        innerHtmlWithLatLongData = jsoninfo.get_attribute("innerHTML")
        latLongIndex = innerHtmlWithLatLongData.find('latlng":{')

        latitude = innerHtmlWithLatLongData[latLongIndex+20: latLongIndex+30]
        longitude_text = innerHtmlWithLatLongData[latLongIndex+20: latLongIndex+200]

        longitude_index = longitude_text.find('longitude":')
        longitude = longitude_text[longitude_index + 11: longitude_index + 22]

        if(latitude == '":{"subpat'):
            latitude = "Latitude_error"
            longitude = "Longitude_error"
        print(name_list[i],"    ", latitude," ", longitude)
    except:
        print(name_list[i],"    ", "Latitude_error"," ", "Longitude_error")
    time.sleep(3)

    i = i + 1

    if i == 192:
        break
