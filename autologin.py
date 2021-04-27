import time
import keyboard
from selenium import webdriver
username = input("enter your username: ")
password = input("enter your account password: ")
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
browser.maximize_window()
time.sleep(3)
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password)
keyboard.press_and_release("enter")



