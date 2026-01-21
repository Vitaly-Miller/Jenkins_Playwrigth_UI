"""
<Login> page
http://localhost:8080/login
"""
from pages.base_page import BasePage
from data.base_data import Base

#=======================================================================================================================
class LoginPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/login'
    TITLE_TEXT = 'Sign in - Jenkins'
    HEADER_TEXT = 'Sign in to Jenkins'

    #---------------- ㉧ LOCATORS: ----------------
    # -Fields-
    @property
    def user_name_field(self):
        return self.page.locator('#j_username')
    @property
    def password_field(self):
        return self.page.locator('#j_password')
    @property
    def keep_signed_checkbox(self):
        return self.page.locator('label[for="remember_me"]')

    # -Buttons-
    @property
    def sign_in_btn(self):
        return self.page.locator('button[name="Submit"]')


    #===================================================== ✨HELPERS ===================================================
    """ Open <Login> page """
    def open(self):
        self.open_page(self.ENDPOINT)                            # -→ <Login> page                                            http://localhost:8080/login

    """ Log in (Authorization) on the Login Page """        # Admin data by Default
    def user_log_in(
            self,
            username: str = Base.USERNAME,
            password: str = Base.PASSWORD
    ):
        self.open()                                         # -→ <Login> page                                            http://localhost:8080/login
        self.user_name_field.fill(username)                 # Fill username field
        self.password_field.fill(password)                  # Fill password field
        self.keep_signed_checkbox.click()                   # Checkbox "Keep me signed in" (optional)
        self.sign_in_btn.click()                            # Click <Sign in> button -→ <Main> page (Dashboard)          http://localhost:8080