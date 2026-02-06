"""
<Main> page (Dashboard)
http://localhost:8080/
"""
from pages.base_page import BasePage

#=======================================================================================================================
class MainPage(BasePage):
    # ------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/'
    TITLE_TEXT = 'Dashboard - Jenkins'
    DEFAULT_HEADER_TEXT = 'Welcome to Jenkins!'                                   # When NO items (jobs)

    # ---------------- ㉧ LOCATORS: ----------------
    @property
    # -Header-
    def default_header(self):
        return self.page.get_by_role("heading", name='Welcome to Jenkins!')  # When NO items (jobs)

    # -Table-
    def table_item_name_link(self, item_name: str):
        return self.page.locator(f'span:has-text("{item_name}")')                 # Open existing Item page              http://localhost:8080/view/all/job/=ITEM_NAME=


    # --Item table Dropdown menu--
    def item_dropdown_menu_chevron(self, item_name: str):
        return self.page.locator(f'[data-href$="/job/{item_name}/"]')


    #===================================================== ✨HELPERS ===================================================
    """ Open <Main> page (Dashboard) """
    def open(self):
        self.open_page(self.ENDPOINT)                                             # Open <Main> page (Dashboard)         http://localhost:8080/