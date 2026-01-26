"""
<New Item> page
http://localhost:8080/view/all/newJob
"""
from pages.base_page import BasePage
from data.generators import Fake

#=======================================================================================================================
class NewItemPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/view/all/newJob'
    TITLE_TEXT = 'New Item - Jenkins'
    HEADER_TEXT = 'New Item'

    #------------- 🅔 DATA (Errors): --------------
    ERROR_TEXT_COLOR_RED = 'oklch(0.6 0.2671 30)'                               # use <.to_have_css>
    INVALID_ITEM_NAME_ERROR_TEXT = 'is an unsafe character'                     # use <.to_contain_text>
    EXIST_ITEM_MANE_ERROR_TEXT = 'A job already exists with the name'           # use <.to_contain_text>

    #---------------- ㉧ LOCATORS: ----------------
    # -Fields-
    @property
    def enter_item_name_field(self):
        return self.page.locator('#name')

    # -Item Types (radio buttons-links)-
    @property
    def freestyle_project_link(self):
        return self.page.get_by_text('Freestyle project', exact=True)
    @property
    def pipeline_link(self):
        return self.page.get_by_text('Pipeline', exact=True)
    @property
    def multi_configuration_project_link(self):
        return self.page.get_by_text('Multi-configuration project', exact=True)
    @property
    def folder_link(self):
        return self.page.get_by_text('Folder', exact=True)

    # -Buttons-
    @property
    def ok_btn(self):
        return self.page.locator('#ok-button')

    # -Errors-
    @property
    def invalid_item_name_error_msg(self):
        return self.page.locator('#itemname-invalid')


    #===================================================== ✨HELPERS ===================================================
    """ Open <New Item> page """
    def open(self):
        self.open_page(self.ENDPOINT)                          # Open <New Item> page                                      http://localhost:8080/view/all/newJob

    # CREATE ITEMS (by Types): (⚠️ Don't forget open page)
    """ Create Freestyle project """
    def create_freestyle_project(self, item_name: str = Fake.item_name):
        self.enter_item_name_field.fill(item_name)             # Fill Item name field
        self.freestyle_project_link.click()                    # Select <Freestyle project>
        self.ok_btn.click()                                    # Click <OK> button -→ <Configuration - General> page     http://localhost:8080/job/gbvn/configure

    """ Create Pipeline """
    def create_pipeline(self, item_name: str = Fake.item_name):
        self.enter_item_name_field.fill(item_name)             # Fill Item name field
        self.pipeline_link.click()                             # Select <Pipeline>
        self.ok_btn.click()                                    # Click <OK> button -→ <Configuration - General> page     http://localhost:8080/job/gbvn/configure

    """ Create Multi-configuration project """
    def create_multi_configuration_project(self, item_name: str = Fake.item_name):
        self.enter_item_name_field.fill(item_name)             # Fill Item name field
        self.multi_configuration_project_link.click()          # Select <Multi-configuration project>
        self.ok_btn.click()                                    # Click <OK> button -→ <Configuration - General> page     http://localhost:8080/job/gbvn/configure

    """ Create Folder """
    def create_folder(self, item_name: str = Fake.item_name):
        self.enter_item_name_field.fill(item_name)             # Fill Item name field
        self.folder_link.click()                               # Select <Folder>
        self.ok_btn.click()                                    # Click <OK> button -→ <Configuration - General> page     http://localhost:8080/job/gbvn/configure


    #-------------------------------------------------------------------------------------------------------------------