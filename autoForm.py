from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import random
import re
from unidecode import unidecode

KHOA = {
    "khoacokhi": 3,
    "khoadiendientu": 4,
    "khoakythuatxaydung": 5,
    "khoacongnghehoahocmoitruong": 6,
    "khoasuphamcongnghiep": 7,
    "khoacongngheso": 8,
}

def openBrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r"executable_path=E:\\3.LAPTRINH\\PYTHON\\chromedriver-win64\\chromedriver.exe")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdyMLPCuRnYBWpwbjay-WjlNRBuYRiseKNRARa1OyGXwa8l8g/viewform")
    driver.implicitly_wait(10)
    return driver

def fillForm1(ten, ngaysinh, khoa, masv, sdt, driver):
    user_name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    user_name.send_keys(ten)
    time.sleep(0.5)
    ngay_thang_nam_sinh = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    ngay_thang_nam_sinh.send_keys(ngaysinh)
    time.sleep(0.5)
    khoa_dang_hoc = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    khoa_dang_hoc.click()
    option = driver.find_element(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[{KHOA[khoa]}]/span')
    option.click()
    time.sleep(0.5)
    ma_sinh_vien = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ma_sinh_vien.send_keys(masv)
    time.sleep(0.5)
    so_dien_thoai = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    so_dien_thoai.send_keys(sdt)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(8)

def fillForm2(driver):
    cau_hoi = driver.find_elements(By.CSS_SELECTOR, 'div.SG0AAe')
    for i in range(len(cau_hoi)):
        tra_loi = cau_hoi[i].find_elements(By.CSS_SELECTOR,'div.hYsg7c')[random.randint(0, 3)]
        tra_loi.click()
        time.sleep(1)
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    submit.click()
    time.sleep(5)

def fac(chuoi):
    chuoi = re.sub(r'\W+', '', chuoi)
    chuoi = chuoi.lower()
    return unidecode(chuoi)

file = open('danhsach.csv', mode='r', encoding='utf-8')
reader = csv.reader(file)
for row in reader:
    driver = openBrowser()
    fillForm1(row[0], row[1], fac(row[2]), row[3], row[4], driver)
    fillForm2(driver)
    driver.close()

print("Done")