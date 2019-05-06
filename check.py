import unittest
from appium import webdriver
from time import sleep


class Btest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        desired_caps= {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] ='C:\\Users\\Mural\Downloads\\build.apk'
        desired_caps['deviceName'] = 'Pixel_2_API_23'
        #desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.onboarding.activity.SplashActivity'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(60)

    @classmethod
    def tearDownClass(cls):
        sleep(10)
        cls.driver.quit()

    # def test01_verify_Onboarding(self):
    #     self.driver.implicitly_wait(60)
    #     ldeny=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
    #     ldeny.click()
    #     allow=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #     allow.click()
    #     self.driver.implicitly_wait(60)
    #     onboard1=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard1.click()
    #     onboard2=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard2.click()
    #     onboard3=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard3.click()
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvRegister").click()
    #     self.driver.find_element_by_xpath("//android.widget.Button[@text='8th']").click()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etName").send_keys("check")
    #     phno=self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").clear()
    #     phno.send_keys("1265291735")
    #     emil=self.driver.find_element_by_id("com.byjus.thelearningapp:id/etEmail")
    #     emil.send_keys("raj@gmail.com")
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etCity").send_keys("ba")
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     self.driver.implicitly_wait(10)
    #     allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #     allow.click()
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element_by_class_name("android.view.ViewGroup").click()
    #     self.driver.implicitly_wait(1000)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Mathematics']").click()
    # def test02_journeylist(self):
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Mathematics']").click()
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='Numbers and Its Properties']").click()
    #     self.driver.implicitly_wait(500)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/action_morph_btn").click()
    #     self.driver.implicitly_wait(60)
    #     self.driver.find_element_by_xpath("//android.view.View[@index=2]").click()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_xpath("//android.view.View[@text='Submit']").click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_xpath("//android.view.View[@text='Next']").click()
    #
    #
    #
    #
    #
    #     # str1 = "SKIP"
    #     # # str2=self.driver.find_element_by_link_text("SKIP")
    #     # ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")')
    #     # str2 = ele.text
    #     # print(str1)
    #     # print(str2)
    #     # if str1 == str2:
    #     #     print("Skip text is present")
    #     #     sleep(2)
    #     #     ele.click()
    #     #     sleep(10)
    #     # else:
    #     #     print("strings are not equal")

# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(Btest)
#     unittest.TextTestRunner(verbosity=2).run(suite)




