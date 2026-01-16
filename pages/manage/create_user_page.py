"""
<Create User> page
http://localhost:8080/manage/securityRealm/addUser
"""
from pages.base_page import BasePage
from data.generators import Fake

#=======================================================================================================================
class CreateUserPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/manage/securityRealm/addUser'
    TITLE_TEXT = 'Create User - Jenkins'
    HEADER_TEXT = 'Create User'

    #------------- 🅔 DATA (Errors): --------------
    PASSWORD_ERROR_MSG_TEXT = ["Password didn't match", "Password didn't match"]

    #---------------- ㉧ LOCATORS: ----------------
    # -User data fields-
    @property
    def username_field(self):
        return self.page.locator('input[id="username"]')
    @property
    def password_field(self):
        return self.page.locator('input[name="password1"]')
    @property
    def confirm_password_field(self):
        return self.page.locator('input[name="password2"]')
    @property
    def full_name_field(self):
        return self.page.locator('input[name="fullname"]')
    @property
    def email_field(self):
        return self.page.locator('input[name="email"]')

    # -Buttons-
    @property
    def create_user_btn(self):
        return self.page.locator('button[name="Submit"]')

    # -Errors-
    @property
    def password_error_msg(self):
        return self.page.locator('div.error')   # ⚠ <Password> & <Confirm Password> error messages => list = ["x", "x"]


    #===================================================== ✨HELPERS ===================================================
    """ Open <Create User> page """
    def open_page(self):
        self.open(self.ENDPOINT)                                # -→ <Create User> page                                  http://localhost:8080/manage/securityRealm/addUser

    """ Fill all fields with User data (Fake data by default) """
    def fill_user_data_fields(
            self,
            username: str = Fake.username,                      # Default args:
            password: str = Fake.user_password,
            confirm_password: str = Fake.user_password,
            full_name: str = Fake.user_full_name,
            email: str = Fake.user_email
    ):
        self.username_field.fill(username)                      # Filling:
        self.password_field.fill(password)
        self.confirm_password_field.fill(confirm_password)
        self.full_name_field.fill(full_name)
        self.email_field.fill(email)
        self.create_user_btn.click()                            # -→ <Jenkins’ own User Database> page                   http://localhost:8080/manage/securityRealm
#-----------------------------------------------------------------------------------------------------------------------