class onboardScreen:
    def __init__(self,driver):
        self.driver=driver
        self.onboard_scrn1txt_id="com.byjus.thelearningapp:id/textViewDetail"
        self.onboard_scrn2txt_id="com.byjus.thelearningapp:id/textViewDetail"

        self.onboard1_screen_btn_id="com.byjus.thelearningapp:id/buttonGetStarted"

    def onboard1_next_btn_click(self):
        self.driver.find_element_by_id(self.onboard1_screen_btn_id).click()
    def onboard2_next_btn_click(self):
        self.driver.find_element_by_id(self.onboard1_screen_btn_id).click()
    def onboard1_txt_valid(self):
        act_txt=self.driver.find_element_by_id(self.onboard_scrn1txt_id)
        actl_txt=act_txt.get_attribute('text')
        print(actl_txt)
        act2_txt = actl_txt.split()
        actual_txt= " ".join(act2_txt)
        print(actual_txt)
        exp_txt = "Engaging videos that make learning simple and fun"
        assert exp_txt in actual_txt
    def onboard2_txt_valid(self):
        act_txt=self.driver.find_element_by_id(self.onboard_scrn2txt_id)
        act_onbtxt2_txt=act_txt.get_attribute('text')
        print(act_onbtxt2_txt)
        actual_txt2=act_onbtxt2_txt.split()
        actual2_txt = " ".join(actual_txt2)
        print(actual2_txt)
        exp_txt = "Unique learning journeys created just for you!"
        assert exp_txt in actual2_txt










