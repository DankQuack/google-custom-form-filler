import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

#(1)change this according to your needs.
df = pd.read_csv('source.csv')

values = df.values

option = webdriver.ChromeOptions()  #(2) initialize webdriver, here i am using chrome but you can use any engine you desire
option.add_argument("-incognito")   #(2.a)
option.add_argument("--headless")  #(2.b)
#option.add_argument("disable-gpu") #(2.c)

driver = webdriver.Chrome(values[0][0],options=option)

driver.get(values[0][1])

small_fields = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
large_fields = driver.find_elements_by_class_name('quantumWizTextinputPapertextareaInput')
submit_btn = driver.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')

#() this dict can possibly be taken from a file if needed
details = [
     "Quack",
    "101",
    "123@123.com",
    "Baker Street"
]

#() from here the code becomes custom as the layout depends
for i in range(0, 3):
    small_fields[i].send_keys(details[i])

large_fields[0].send_keys(details[3])

submit_btn.click()

driver.close()
