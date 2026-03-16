"""
<New> page
https://website.com/=NEW_PAGE=
"""
from pages.base_page import BasePage

#=======================================================================================================================
class NewPage(BasePage):
    # -------------------------------------------------- 𝌆 DATA --------------------------------------------------------
    ENDPOINT = ''
    TITLE_TEXT = ''
    HEADER_TEXT = ''

    # ----------------------------------------------- 🅔 ERROR data ----------------------------------------------------


    # ------------------------------------------------ ㉧ LOCATORS ------------------------------------------------------
    # ---- Buttons ----
    @property
    def xxx_btn(self):
        return self.page.locator('')

    # ---- Fields ----

    # ---- Errors ----


    #================================================== ✨HELPERS ======================================================
    # Open <New> page
    def open(self):
        return self.open_page(self.ENDPOINT)            # -→ <New> page                                                  https://website.com/=NEW_PAGE=
