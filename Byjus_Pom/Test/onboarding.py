import unittest
from appium import webdriver
from time import sleep
from Byjus_Pom.Pages.Apppermission import Apppermission
from Byjus_Pom.Pages.onboardScreen import onboardScreen
import subprocess


class Byjusapptest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        subprocess.Popen('appium', shell=True)
        sleep(5)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = 'C:\\Users\\Mural\Downloads\\build.apk'
        desired_caps['deviceName'] = 'Pixel_2_API_23'
        # desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.onboarding.activity.SplashActivity'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(60)





    def test01_apppermission_deny(self):
        #verifying by denying all the permission
        driver=self.driver
        app_per =Apppermission(driver)
        app_per.loc_deny_click()
        app_per.cont_deny_click()
        driver.launch_app()
    def test02_apppermission_accept(self):
        #verifying by denying location and allowing contacts
        driver=self.driver
        app_per=Apppermission(driver)
        app_per.loc_deny_click()
        app_per.cont_allow_click()
        driver.launch_app()
    def test03_apppermission_allow(self):
        #verifying by allowing all the permission
        driver=self.driver
        app_per=Apppermission(driver)
        app_per.cont_allow_click()
        app_per.cont_allow_click()

    def test04_onboarding_screen1_verify(self):
        #verify onboarding screen1 and validate text
        driver=self.driver
        scr1= onboardScreen(driver)
        scr1.onboard1_txt_valid()
        scr1.onboard1_next_btn_click()
    def test05_onboarding_screen2_verify(self):
        #verify onboarding screen2 and validate text
        driver=self.driver
        scr2=onboardScreen(driver)
        scr2.onboard2_txt_valid()
        scr2.onboard2_next_btn_click()

    @classmethod
    def tearDownClass(cls):
        sleep(10)
        cls.driver.quit()
        #subprocess.Popen('killall node.exe', shell=False)
        subprocess.Popen('Taskkill /IM node.exe /F', shell=True)