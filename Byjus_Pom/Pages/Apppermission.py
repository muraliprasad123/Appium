class Apppermission:

    def __init__(self, driver):
        self.driver=driver
        self.loc_deny_btn_id ="com.android.packageinstaller:id/permission_deny_button"
        self.loc_allow_btn_id ="com.android.packageinstaller:id/permission_allow_button"
        self.cont_allow_btn_id="com.android.packageinstaller:id/permission_allow_button"
        self.cont_deny_btn_id="com.android.packageinstaller:id/permission_deny_button"
    def loc_deny_click(self):
        self.driver.find_element_by_id(self.loc_deny_btn_id).click()
    def loc_allow_click(self):
        self.driver.find_element_by_id(self.cont_allow_btn_id).click()
    def cont_allow_click(self):
        self.driver.find_element_by_id(self.loc_allow_btn_id).click()
    def cont_deny_click(self):
        self.driver.find_element_by_id(self.cont_deny_btn_id).click()






