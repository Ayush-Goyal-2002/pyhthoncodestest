
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ID = "ag.9458291321@gmail.com"
PASS = "Ayush@123"
SEARCH = "DATA ANALYST"

chrome_driver_path  = "C:/Users/ASUS/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)





#driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
# fname = driver.find_element(By.XPATH,"/html/body/form/input[1]")
# lname = driver.find_element(By.XPATH,"/html/body/form/input[2]")
# email = driver.find_element(By.XPATH,"/html/body/form/input[3]")
#
#
# button = driver.find_element(By.XPATH,"/html/body/form/button")
#
#
#https://www.linkedin.com
# fname.send_keys("Ayush")
# lname.send_keys("Goyal")
# email.send_keys("ag.@gmail.com")
# button.click()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
#driver.get("https://www.linkedin.com")
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

time.sleep(3)
email = driver.find_element(By.ID,'username' )
email.send_keys(ID)
password = driver.find_element(By.ID,"password")
password.send_keys(PASS)
button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
button.click()
time.sleep(2)
search= driver.find_element(By.XPATH,"/html/body/div[5]/header/div/div/div/div[2]/div[1]/div/div/input[1]")
search_button = driver.find_element(By.XPATH,"/html/body/div[5]/header/div/div/div/div[2]/button[1]")
search.send_keys(SEARCH)
search_button.send_keys(Keys.ENTER)







sign_in_button.click()









# driver.quit()