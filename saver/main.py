from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def operate():
    driver = webdriver.Chrome(executable_path=r"C:\Users\manuel\Downloads\chromedriver_win32\CHROMEDRIVER.EXE")
    driver.get("https://waeup.uniben.edu/login")

    element1 = driver.find_element(By.NAME, "form.login")
    element1.clear()
    element1.send_keys("B1145429")

    element2 = driver.find_element(By.NAME, "form.password")
    element2.clear()
    element2.send_keys("896313")

    element3 = driver.find_element(By.NAME, "SUBMIT")

    element3.click()

    element1a = driver.find_element(By.LINK_TEXT, "My Data")

    element1a.click()

    element1b = driver.find_element(By.LINK_TEXT, "Accommodation Data")

    element1b.click()




    book = driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div/div/div/form/input")
    book.click()


    hos = driver.find_element(By.NAME,"ac_series")
    hos.send_keys("0")

    code = driver.find_element(By.NAME, "ac_number")
    code.send_keys("9527213010")

    submitt = driver.find_element(By.NAME, "SUBMIT")
    submitt.click()

    driver.implicitly_wait(2)

    try:
        alertt = driver.find_element(By.CLASS_NAME, "alert alert-warning")
    except:
        print("trying again")
        v = 1
    else:
        print("Success")
        v = 0


    while(v == 1):
        book = driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div/div/div/form/input")
        book.click()


        hos = driver.find_element(By.NAME,"ac_series")
        hos.send_keys("0")

        code = driver.find_element(By.NAME, "ac_number")
        code.send_keys("9527213010")

        submitt = driver.find_element(By.NAME, "SUBMIT")
        submitt.click()

        driver.implicitly_wait(2)

        try:
            alertt = driver.find_element(By.CLASS_NAME, "alert alert-warning")
        except:
            print("trying again")
            v = 1
        else:
            print("Success")
            v = 0
