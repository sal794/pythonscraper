import sys
sys.path.append('C:/Users/sam.luebbers/appdata/local/programs/python/python36-32/lib/site-packages')
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from bs4 import NavigableString

driver = webdriver.Chrome('C:\\Users\\Sam.Luebbers\\Desktop\\DataClass\\chromedriver.exe')

driver.get('https://www.niche.com/colleges/search/top-party-schools/')
wait = WebDriverWait(driver, 100)
soup = BeautifulSoup(driver.page_source, 'lxml')
workbook = xlsxwriter.Workbook('Party_Schools.xlsx')
worksheet = workbook.add_worksheet()
answers = []
locations = []
for i in range(60):
    try:
        #sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tags = soup.find_all(class_='search-result-entity-name')
        places = soup.find_all(class_='card__inner')
        for tag in tags:
            answers.append(tag.string)
        for place in places:
            locations.append(place.li.next_sibling.string)
        next_button = driver.find_element_by_class_name('icon-arrowright-thin--pagination')
        driver.execute_script("arguments[0].click()", next_button)
    except NoSuchElementException:
        break
driver.close()
for row in range(len(answers)):
    worksheet.write(row, 0, row + 1)
    worksheet.write(row, 1, answers[row])
    worksheet.write(row, 2, locations[row])
workbook.close()
