"""
<Main> page (Dashboard)
http://localhost:8080/
"""
from pages.base_page import BasePage

#=======================================================================================================================
class MainPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/'
    TITLE_TEXT = 'Dashboard - Jenkins'
    DEFAULT_HEADER_TEXT = 'Welcome to Jenkins!'                                   # When NO jobs

    #---------------- ㉧ LOCATORS: ----------------
    @property
    # -Header-
    def default_header(self):
        return self.page.get_by_role("heading", name='Welcome to Jenkins!')  # When NO jobs

    # -Table-
    def table_item_name_link(self, item_mame: str):
        return self.page.locator(f'span:has-text("{item_mame}")')                 # -→ <Item> page                       http://localhost:8080/view/all/job/=ITEM_NAME=


    #===================================================== ✨HELPERS ===================================================
    """ Open <Main> page (Dashboard) """
    def open_page(self):
        return self.open(self.ENDPOINT)                                           # -→ <Main> page (Dashboard)           http://localhost:8080/
