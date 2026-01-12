"""
<Jenkins’ own User Database> page (Table)
http://localhost:8080/manage/securityRealm/
"""
from pages.base_page import BasePage

#=======================================================================================================================
class UserDatabasePage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/manage/securityRealm/'
    TITLE_TEXT = 'Users - Jenkins'
    HEADER_TEXT = 'Users'

    #---------------- ㉧ LOCATORS: ----------------
    # -Users table-
    @property
    def users_table(self):
        return self.page.locator('#people')

    # -Buttons-
    @property
    def create_user_btn(self):
        return self.page.get_by_role("link", name="Create User")

    # -Table elements-
    def table_user_id(self, username: str):
        return self.page.locator(f'td > a[href="user/{username.lower()}/"]')
    def table_user_name(self, user_name: str):
        return self.page.locator(f'//td[normalize-space()="{user_name}"]')

    # --Table User ID Dropdown menu--
    def user_dropdown_menu_chevron(self, username: str):
        return self.page.locator(f'button[data-href$="user/{username.lower()}/"]')
    def dropdown_menu_delete_btn(self, username: str):
        return self.page.locator(f'button[href="/user/{username.lower()}/doDelete"]')
    @property
    def delete_yes_bnt(self):
        return self.page.locator('button[data-id="ok"]')
    @property
    def delete_cancel_btn(self):
        return self.page.locator('button[data-id="cancel"]')


    #===================================================== ✨HELPERS ===================================================
    """ Open <Jenkins’ own User Database> page """
    def open_page(self):
        self.page.goto(self.ENDPOINT)                      # -→ <Jenkins’ own user database> page                        http://localhost:8080/manage/securityRealm

    """ Delete User """
    def delete_user(self, username: str):
        self.user_dropdown_menu_chevron(username).click()  # Open user dropdown menu
        self.dropdown_menu_delete_btn(username).click()    # Click <Delete> button
        self.delete_yes_bnt.click()                        # Click <Yes> button (Confirm deletion)
