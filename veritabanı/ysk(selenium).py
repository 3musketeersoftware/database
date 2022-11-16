from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(executable_path="C:/Users/YSARS/Desktop/DENEME/chromedriver.exe")
driver.maximize_window()
driver.get("https://sonuc.ysk.gov.tr/sorgu")


gir=driver.find_element(By.XPATH,'//*[@id="collapsePanelTwo"]/div/div/div[2]/button/div/div')
    
gir.click()    
sleep(1)
select = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div/div/ng-select')
    
select.click()
    # 2018 seçimlerinin radyo düğmesine tıkla.
sleep(1)

secimbutton = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div[1]/div/ng-select/div/div/div[2]/input')
secimbutton.send_keys("24.DÖNEM MİLLETVEKİLİ GENEL SEÇİMİ")


sleep(1)
secimbutton.send_keys(Keys.ENTER)
    
sleep(1)
yurtici = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div[2]/div/div[2]/label')
yurtici.click()
    
sleep(1)
devamet= driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[2]/div/div/button[1]')
devamet.click()
sleep(2)
driver.execute_script("window.scrollTo(0, 1);")
    
indir=driver.find_element(By.XPATH,'//*[@id="collapsePanelFour"]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[2]/div/button')
indir.click()
    
    
onayla=driver.find_element(By.XPATH,'/html/body/ngb-modal-window/div/div/div[2]/div/button[1]')
onayla.click()
    
sleep(3)
son=driver.find_element(By.XPATH,'//*[@id="headingPanelThree"]/div/div[1]/h5/button/span')
son.click()
for i in range(2):
    sil = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div[1]/div/ng-select/div/span[1]')
    sil.click()
    sleep(2)
    
    secimbutton = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div[1]/div/ng-select/div/div/div[2]/input')
    secimbutton.send_keys("2",(i+5),".DÖNEM MİLLETVEKİLİ GENEL SEÇİMİ")
    sleep(1)
    secimbutton.send_keys(Keys.ENTER)
    
    sleep(1)
    yurtici = driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[1]/div[2]/div/div[2]/label')
    yurtici.click()
    
    sleep(1)
    devamet= driver.find_element(By.XPATH,'//*[@id="collapsePanelThree"]/div[1]/div/div/form/div[2]/div/div/button[1]')
    devamet.click()
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1);")
    
    indir=driver.find_element(By.XPATH,'//*[@id="collapsePanelFour"]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[2]/div/button')
    indir.click()
    
    
    onayla=driver.find_element(By.XPATH,'/html/body/ngb-modal-window/div/div/div[2]/div/button[1]')
    onayla.click()
    
    sleep(3)
    son=driver.find_element(By.XPATH,'//*[@id="headingPanelThree"]/div/div[1]/h5/button/span')
    son.click()
# "Tamam" düğmesine tıkla

