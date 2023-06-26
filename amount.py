from time import sleep
import xlwings as xw
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import filedialog
from tkinter import *

#------------------------------------------------------------------------------------------------------------------------------


# ========== ********************* ===========
# ----------  Automation FUNCTION  -----------
# ========== ********************* ===========
def automation(CARD_NO,PIN_NO,numb,ws):
    try:
        driver.get("https://www.woohoo.in/balenq")

        #<------------ LOGIN ------------>

        c_num = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="cardNumber"]'))
                )
        c_num.send_keys(CARD_NO)

        #<------------ PASSWORD ------------>

        pin_num = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="cardPin"]'))
                )
        pin_num.send_keys(PIN_NO)


    except Exception as e:
        print('Failed due to ' + str(e))
        return 0

# ========== *********************** ===========
# ----------     FUNCTION ENDING     -----------
# ========== *********************** ===========

#------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------  ##########################  ------------------------------------
# -------------------------------------  **************************  ------------------------------------
# =====================================  Start Automation Function   ====================================
# -------------------------------------  **************************  ------------------------------------
# -------------------------------------  ##########################  ------------------------------------




file_path = filedialog.askopenfilename(defaultextension='.xlsx',title="Choose Login Excel File")
wb = xw.Book(file_path)
ws = wb.sheets("data")
rows = ws.range("A1").expand().options(numbers=int).value
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.minimize_window()

num = 1
for row in rows:
    if num == 1:
        num+=1
        continue
    login = row[0]
    passwd = row[1]

    automation(login,passwd,num,ws)
    num += 1

wb.save()
wb.close()
driver.close()
