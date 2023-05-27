from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class Scrape():
        def __init__(self) -> None:
            self.options = webdriver.FirefoxOptions()
            self.profile = webdriver.FirefoxProfile()
            # self.profile.set_preference("browser.download.folderList",2)
            # self.profile.set_preference("javascript.enabled", False)
            self.options.add_argument("-headless") #makes this headless (disable when debugging)
            self.driver = webdriver.Firefox(options = self.options, firefox_profile= self.profile)
            self.driver.implicitly_wait(4)
            self.driver.get('https://www.investing.com/currencies/streaming-forex-rates-majors')

        def refresh(self):
            self.driver.refresh()

        
        def fetch(self):
    
            head = []
            table_head = self.driver.find_element(By.CSS_SELECTOR, ".dynamic-table_dynamic-table__7SSn8 > thead:nth-child(1) > tr:nth-child(1)")
            head_items = table_head.find_elements(By.TAG_NAME, 'th')
            for item in head_items:
                head.append(item.text)
    
            data = pd.DataFrame(columns = head)
            
            table = self.driver.find_element(By.CSS_SELECTOR, ".dynamic-table_dynamic-table__7SSn8 > tbody:nth-child(2)")
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                row_data = []
                cols = row.find_elements(By.TAG_NAME, 'td')
                for col in cols:
                    row_data.append(col.text)
                data.loc[len(data) + 1] = row_data
            
            data.to_csv('live_data.csv')
            return data
            

        def quit(self):
            self.driver.quit()

