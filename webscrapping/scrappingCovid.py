from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://coronavirus.es.gov.br/painel-covid-19-es")

csv_covid = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[3]/div/article/div/div/div/div/div/div['
                                          '1]/p/a[1]').click()
sleep(3)
