import unittest
from check import Btest

class Onboarding_course(Btest):


    # def test01_apppermissiomdeny(self):
    #     #verify user denys the permission
    #     loc_deny = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
    #     loc_deny.click()
    #     con_deny= self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
    #     con_deny.click()
    #     print("App Permission deny sucessfully")
    #     self.driver.launch_app()
    #
    #
    #
    # def test02_apppermissionaccept1(self):
    #     #verify user accepts onre of the permission
    #     loc_deny = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
    #     loc_deny.click()
    #     con_allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #     con_allow.click()
    #     print("app permission accept1 verified")
    #     self.driver.launch_app()


    def test03_apppermissionallow(self):
        #verify user accepts all the required permission
        loc_allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        loc_allow.click()
        con_allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        con_allow.click()
        print("App permission allowed sucessfully")


    # def test04_onboardscreens(self):
    #     #Verify 3 onboarding screens
    #     onboard1_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard1_screen.click()
    #     onboard2_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard2_screen.click()
    #     onboard3_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard3_screen.click()
    #     print("onboarding screens verified ")
    #     self.driver.launch_app()
    # def test05_onboardingscreen_skip(self):
    #     #verify on tapping on skip user is landed on course selection screen
    #
    #     loc_allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #     loc_allow.click()
    #     con_allow = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #     con_allow.click()
    #     skip_btn=self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonSkip")
    #     skip_btn.click()
    #     print("Clicked on skipped")
    #     self.driver.launch_app()
    # def test06_Onboardingscreen1_txt_valid(self):
    #     #verifying the text in 1st onboarding screen.
    #     exp_txt = "Engaging videos that make learning simple and fun"
    #
    #     ob1text=self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail")
    #     act_txt=ob1text.get_attribute('text')
    #     print(act_txt)
    #     act2_txt = act_txt.split()
    #     print(act2_txt)
    #     actual_txt = " ".join(act2_txt)
    #     print(actual_txt)
    #     assert exp_txt in actual_txt
    #     print("verified text on Onboarding screen1 sucessfully")
    #     onboard1_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard1_screen.click()
    #
    # def test07_Onboardingscreen2_txt_valid(self):
    #     #Verify text in onbarding screen2
    #     exp_txt = "Unique learning journeys created just for you!"
    #     ob2_text = self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail")
    #     act_text = ob2_text.get_attribute('text')
    #     print(act_text)
    #     act2_txt = act_text.split()
    #     print(act2_txt)
    #     actual_txt = " ".join(act2_txt)
    #     print(actual_txt)
    #     assert actual_txt in exp_txt
    #     print("verified text on Onboarding screen2 sucessfully")
    #     onboard2_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     onboard2_screen.click()
    #
    # def test08_Onboardingscreen2_txt_valid(self):
    #     # Verify text in onbarding screen3
    #     exp_txt = "Customized feedback with recommendations at every step "
    #     ob2_text = self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail")
    #     act_text = ob2_text.get_attribute('text')
    #     print(act_text)
    #     act2_txt = act_text.split()
    #     print(act2_txt)
    #     actual_txt = " ".join(act2_txt)
    #     print(actual_txt)
    #     assert actual_txt in exp_txt
    #     print("verified text on Onboarding screen3 sucessfully")
    #     # onboard2_screen = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
    #     # onboard2_screen.click()
    def test09_onboard_swipe(self):
        #swipe the screens until Getstarted is seen
        while True:
            # Vertical swipe until the required element is found
            size = self.driver.get_window_size()
            endx1 = int(size["width"] * 0.10)
            startx1 = int(size["width"] * 0.90)
            starty = int(size["height"] * 0.50)
            self.driver.swipe(startx1, starty, endx1, starty, 1000)
            print("check swipe")
            checktext = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
            txt = checktext.get_attribute('text')
            exp_txt = "Get Started"
            print(txt)
            if txt == exp_txt:
                print("got the required text")
                break

        #swipe from down to up
        # size = self.driver.get_window_size()
        # endx1 = int(size["width"] * 0.10)
        # startx1= int(size["width"] * 0.90)
        # starty = int(size["height"] * 0.50)
        # self.driver.swipe(startx1,starty, endx1, starty, 1000)
        # print("check swipe")
        # checktext = self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted")
        # txt = checktext.get_attribute('text')
        # str1= "Get Started"
        # print(txt)
        # if txt == str1:
        #     print("got")
        #     break




















if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Onboarding_course)
    unittest.TextTestRunner(verbosity=2).run(suite)

