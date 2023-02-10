import random
from time import sleep
from loguru import logger
from multiprocessing import Pool
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import json

with open('twitter.txt','r') as file:
    twitter_list = [x.rstrip() for x in file.readlines()]

with open('seeds.txt','r') as file:
    seeds_list = [x.rstrip() for x in file.readlines()]

with open('ua.txt','r') as file:
    ua_list = [x.rstrip() for x in file.readlines()]
with open('config.json','r') as file:
    config_file = json.load(file)
    ref_link = config_file['ref_link']
    API_KEY = config_file['anti_captcha_apikey']
    processes_count = config_file['processes_count']
logger.info('''
THIS SOFTWARE WAS WRITTEN BY FLEXTER
Telegram channel @flexterwork''')


data_list = []
for index, seed in enumerate(seeds_list):
    twitter = twitter_list[index]
    data_list.append(f"{seed};{twitter}")

class Abuser:

    def __init__(self):
        self.ref_link = ref_link
        self.API_KEY = API_KEY

    def browser_creation(self, seed):
        try:
            chrome_options = Options()
            chrome_options.add_argument(f'user-agent={random.choice(ua_list)}')
            chrome_options.add_argument('--disable-blink-feature=AutomationControlled')
            chrome_options.add_extension((os.path.abspath('anticaptcha-plugin_v0.62.crx')))
            chrome_options.add_extension((os.path.abspath('10.18.3_0.crx')))

            self.browser = webdriver.Chrome(service=Service(os.path.abspath('chromedriver')), options=chrome_options)
            self.browser.maximize_window()
            sleep(3)
            self.browser.get('chrome-extension://lncaoejhfdpcafpkkcddpjnhnodcajfg/options.html')
            self.browser.implicitly_wait(5)
            api_key = self.browser.find_element(By.CSS_SELECTOR,
                                           'body > div > div.options_form > input[type=text]:nth-child(7)')
            api_key.send_keys(self.API_KEY)
            log_in_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div > input').click()
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
            self.browser.implicitly_wait(5)
            self.browser.find_element(By.CSS_SELECTOR,
                                      '#app-content > div > div.main-container-wrapper > div > div > div > button').click()
            self.browser.implicitly_wait(3)
            self.browser.find_element(By.CSS_SELECTOR,
                                      '#app-content > div > div.main-container-wrapper > div > div > div > div.metametrics-opt-in__footer > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button').click()
            self.browser.implicitly_wait(3)
            self.browser.find_element(By.CSS_SELECTOR,
                                      '#app-content > div > div.main-container-wrapper > div > div > div.select-action__wrapper > div > div.select-action__select-buttons > div:nth-child(1) > button').click()
            self.browser.implicitly_wait(3)
            seed_phrase_inputs = self.browser.find_elements(By.CLASS_NAME, 'MuiInputBase-input')
            seed_word_list = seed.split(' ')
            for input_field in seed_phrase_inputs[:12]:
                input_field.send_keys(seed_word_list[0])
                del seed_word_list[0]
            for input_field in seed_phrase_inputs[12:]:
                input_field.send_keys('12345678')
            self.browser.find_element(By.CSS_SELECTOR, '#create-new-vault__terms-checkbox').click()
            self.browser.implicitly_wait(10)
            self.browser.find_element(By.CSS_SELECTOR,
                                      '#app-content > div > div.main-container-wrapper > div > div > div.first-time-flow__import > form > button').click()
            self.browser.implicitly_wait(10)
            self.browser.find_element(By.CSS_SELECTOR,
                                      '#app-content > div > div.main-container-wrapper > div > div > button').click()
            self.browser.implicitly_wait(10)
            try:
                self.browser.find_element(By.CSS_SELECTOR,
                                          '#popover-content > div > div > section > div.box.popover-header.box--rounded-xl.box--padding-top-6.box--padding-right-4.box--padding-bottom-4.box--padding-left-4.box--display-flex.box--flex-direction-column.box--background-color-background-default > div > button').click()
            except:
                pass
            if self.browser.find_element(By.CSS_SELECTOR,
                                         '#app-content > div > div.main-container-wrapper > div > div > div > div.home__balance-wrapper > div > div.wallet-overview__balance'):
                logger.info(f'Успешно вошел в метамаск | {seed}')
        except Exception as exc:
            logger.error(exc)
            if self.browser:
                self.browser.quit()

    def twitter_login(self, twitter_data):
        self.browser.get('https://twitter.com/i/flow/login')
        self.browser.implicitly_wait(15)
        login, password, phone = twitter_data.split(':')
        login_input = self.browser.find_element(By.CSS_SELECTOR, '.r-30o5oe').send_keys(login)
        next_button = self.browser.find_element(By.CSS_SELECTOR,
                                           'div.css-18t94o4:nth-child(6) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)').click()
        self.browser.implicitly_wait(10)
        password_input = self.browser.find_element(By.CSS_SELECTOR, '.r-homxoj').send_keys(password)
        login_button = self.browser.find_element(By.CSS_SELECTOR,
                                            'span.css-1hf3ou5:nth-child(1) > span:nth-child(1)').click()
        self.browser.implicitly_wait(10)
        sleep(3)
        if self.browser.page_source.find('Номер телефона') != -1 or self.browser.page_source.find(
                'Адрес электронной почты') != -1:
            phone_input = self.browser.find_element(By.NAME, 'text')
            phone_input.send_keys(phone)
            next = ActionChains(self.browser).move_to_element_with_offset(phone_input, +140, +200).click().perform()
            self.browser.implicitly_wait(10)
            sleep(5)
            if self.browser.page_source.find('Password change required') != -1:
                logger.error(f'Аккаунт заблокирован | {twitter_data}')
            else:
                logger.info(f'Успешно вошел в твиттер аккаунт | {twitter_data}')
                self.browser.get('https://twitter.com/kandyland_io')
                self.browser.implicitly_wait(20)
                sleep(3)
                try:
                    self.browser.find_element(By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1h0z5md.r-dnmrzs > div:nth-child(2) > div.css-1dbjc4n.r-6gpygo > div > div > span > span').click()
                    sleep(2)
                except:
                    pass



    def kandyland_register(self):
        self.browser.get(self.ref_link)
        self.browser.implicitly_wait(20)
        connect = self.browser.find_element(By.CSS_SELECTOR,'#__next > div.hide-overflow > div > div.home-cnt > div > div > div.home-button-cnt > div > a').click()
        sleep(3)
        metamask = self.browser.find_element(By.CSS_SELECTOR,'#__CONNECTKIT__ > div > div > div > div.sc-idXgbr.dWgQgj > div.sc-kDvujY.juXNVx.active > div.sc-csuSiG.hEdpAI > div > div > div > div.sc-hiDMwi.dyPmnV > button:nth-child(1) > span').click()
        sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.find_element(By.CSS_SELECTOR,
                                  '#app-content > div > div.main-container-wrapper > div > div.permissions-connect-choose-account__footer-container > div.permissions-connect-choose-account__bottom-buttons > button.button.btn--rounded.btn-primary').click()
        self.browser.implicitly_wait(10)
        sleep(3)
        self.browser.find_element(By.CSS_SELECTOR,
                                  '#app-content > div > div.main-container-wrapper > div > div.page-container.permission-approval-container > div.permission-approval-container__footers > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button').click()
        sleep(3)
        self.browser.find_element(By.CSS_SELECTOR,'#app-content > div > div.main-container-wrapper > div > div.request-signature__footer > button.button.btn--rounded.btn-primary.btn--large.request-signature__footer__sign-button').click()
        sleep(7)
        self.browser.switch_to.window(self.browser.window_handles[1])
        sleep(5)
        self.browser.implicitly_wait(15)

        if self.browser.page_source.find('Complete the steps to continue')!=-1:
            logger.info('Решаю капчу...')
            while True:
                try:
                    self.browser.find_element(By.CSS_SELECTOR,'#__next > div.hide-overflow > div > div > a > div.twitter-referral-button-text').click()
                    break
                except Exception as exc:
                    pass
            logger.info('Решил капчу')
            self.browser.find_element(By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-1gluylu > div > div > div.css-1dbjc4n.r-1awozwy.r-6koalj.r-q4m81j > div.css-1dbjc4n.r-11rk87y.r-1ur9v65 > div > div > span > span').click()
            self.browser.implicitly_wait(15)
            sleep(10)

            self.browser.find_element(By.CSS_SELECTOR,'#__next > div.hide-overflow > div > div > a.twitter-button.follow-twitter > div.twitter-referral-button-text').click()
            self.browser.implicitly_wait(15)
            sleep(10)
            self.browser.switch_to.window(self.browser.window_handles[1])
            sleep(10)
            self.browser.find_element(By.CSS_SELECTOR,'#__next > div.hide-overflow > div > div > div.box-cnt > div > div.box-bonus-button > a > div.referral-button-text-inner').click()
            self.browser.switch_to.window(self.browser.window_handles[1])
            if self.browser.page_source.find("You've successfully entered the raffle")!=-1:
                logger.success('Успешно зарегался в раффле')
                return True




    def main(self, data):
        try:
            seed, twitter = data.split(';')
            self.browser_creation(seed)
            if self.browser:
                self.twitter_login(twitter)
                if self.kandyland_register() is True:
                    with open('success.txt','a+') as file:
                        file.writelines(f"{data}\n")
        except Exception as exc:
            logger.error(exc)
        finally:
            if self.browser:
                self.browser.quit()


if __name__ == '__main__':
    Pool(processes=processes_count).map(Abuser().main, data_list)
