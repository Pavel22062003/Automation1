from selenium import webdriver

"""Переменные путей"""
url = 'https://shop.foodsoul.pro'
path = 'Полный путь до файла с chromedriver.exe'
#C:\\Users\\Пользователь\\PycharmProjects\\pythonProject\\selenium\\chrome-driver\\chromedriver.exe

"""Настройки options"""
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")


"Настройки для авторизации"

name = 'Имя'

phone = 'телефон'