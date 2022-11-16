from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

seneler_liste=["/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[1]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[2]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[3]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[4]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[5]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[5]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[6]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[7]/td","/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr[8]/td"]
driver = webdriver.Chrome(executable_path="C:/Users/YSARS/Desktop/DENEME/chromedriver.exe")
driver.maximize_window()
driver.get("https://biruni.tuik.gov.tr/secimdagitimapp/secim.zul")

for i in range(9):
    sleep(2)
    secim = driver.find_element(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[6]/td')
    secim.click()
    sleep(2)
    sene=driver.find_element(By.XPATH,seneler_liste[i])
    sene.click()
    sleep(2)
    tumiller = driver.find_element(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr[2]/td/div/div/table/tbody/tr[6]/td/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[1]/td')
    tumiller.click()
    sleep(2)
    excel = driver.find_element(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span/span[2]/input')
    excel.click()
    sleep(2)
    indir = driver.find_element(By.XPATH,'/html/body/div/div/div/div/table/tbody/tr[4]/td/div/div[2]/table/tbody/tr/td[2]/input')
    indir.click()
    sleep(2)
    driver.refresh()