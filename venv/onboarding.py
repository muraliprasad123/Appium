from selenium.webdriver.common.by import By

from check import Btest
import  unittest

class onboarding(Btest):


    def test01_verify_Onboarding(self):
        self.driver.implicitly_wait(60)
        ldeny=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
        ldeny.click()
        allow=self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        allow.click()
        self.driver.implicitly_wait(60)
        onboard1=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
        onboard1.click()
        onboard2=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
        onboard2.click()
        onboard3=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
        onboard3.click()
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvRegister").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@text='8th']").click()
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/etName").send_keys("check")
        phno=self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").clear()
        phno.send_keys("1265291735")
        emil=self.driver.find_element_by_id("com.byjus.thelearningapp:id/etEmail")
        emil.send_keys("raj@gmail.com")
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/etCity").send_keys("ba")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
        self.driver.implicitly_wait(10)
        allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        allow.click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("android.view.ViewGroup").click()
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Mathematics']").click()
        assert 23 not in  self.driver.find_element(By.XPATH, 'ttr').get_text()







