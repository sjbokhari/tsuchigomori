from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def init_spider():
    driver = webdriver.Chrome()
    return driver


def execute_query():
    driver = init_spider()
    driver.get('https://www.gelbeseiten.de')
    driver.find_element(By.XPATH, '//*[@id="cmpwelcomebtnyes"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="what_search"]').send_keys("hotels")
    driver.find_element(By.XPATH, '//*[@id="where_search"]').send_keys("Frankfurt Am Main")
    driver.find_element(By.XPATH, '//*[@id="transform_wrapper"]/section[1]/div/div/div/div[1]/div/div/form/div[2]/div[2]/button').click()
    driver.close()

def main():
    execute_query()

if __name__ == "__main__":
    main()