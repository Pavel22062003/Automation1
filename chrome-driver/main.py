import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

import settings


class FoodOrderAutomation:

    def __init__(self):
        """Инициализация driver и добавление в него необходимых настроек"""
        user_agent = UserAgent()

        service = Service(executable_path=settings.path)  # Here
        self.driver = webdriver.Chrome(service=service, options=settings.options)

        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": user_agent.random}
                                    )

    def open_site(self):
        self.driver.get(url=settings.url)
        time.sleep(15)

    def choose_order_type(self):
        button = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[2]/span')  # самовывоз

        button.click()

        time.sleep(5)

        button2 = self.driver.find_element(By.XPATH,
                                           '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]')  # выбор ресторана

        button2.click()

        time.sleep(3)

    def cookie_delete_and_scroll(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'svg.alert__close')  # убрать cookie
        button.click()
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,1000)')
        time.sleep(1)

    def work_with_order(self):
        button = self.driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[2]/main/div[1]/div/div[3]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/button[2]').click()  # добавление в корзину
        time.sleep(5)

        button2 = self.driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[2]/div[2]/div/div/div/button')  # нажатие на корзину
        button2.click()

        time.sleep(3)

        self.driver.save_screenshot('1.png')

        time.sleep(5)

        button3 = self.driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[2]/div/div/div[2]/div/button').click()  # нажатие на оформить

        time.sleep(10)

    def authorization(self):
        phone = self.driver.find_element(By.XPATH,
                                         '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/input')

        phone.send_keys(settings.name)  # вставление номера телефона
        time.sleep(10)
        phone_accept = self.driver.find_element(By.XPATH,
                                                '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div[2]/div/button[1]').click()
        # нажатие на кнопку телефон
        time.sleep(10)
        alert = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button').click()
        time.sleep(5)
        auth_name = self.driver.find_element(By.XPATH,
                                             '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div/div[1]/input')
        auth_name.send_keys(settings.name)
        time.sleep(2)
        gender = self.driver.find_element(By.XPATH,
                                          '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div/div[3]/div/button'
                                          ).click()

        men = self.driver.find_element(By.XPATH,
                                       '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/ul/li[1]/div/span').click()

        code_input = self.driver.find_element(By.XPATH,
                                              '//*[@id="topBar"]/div/div/div[2]/div/div/div[2]/form/div/div/input')
        print('Нужно сбросить входящий звонок и ввести последние 6 цифр')
        code_input.send_keys(input('Код:'))
        checkout = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div/button').click()
        time.sleep(10)
        self.driver.quit()


exemp = FoodOrderAutomation()
exemp.open_site()

exemp.choose_order_type()

exemp.cookie_delete_and_scroll()

exemp.work_with_order()

exemp.authorization()
