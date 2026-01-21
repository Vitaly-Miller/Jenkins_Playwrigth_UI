"""
<New View> page
http://localhost:8080/job/=ITEM_NAME=/newView
"""
from pages.base_page import BasePage

#=======================================================================================================================
class NewViewPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    @staticmethod
    def endpoint(item_name: str):
        return f'/view/all/job/{item_name}/newView'

    TITLE_TEXT = 'New View - Jenkins'
    HEADER_TEXT = ''

    #------------- 🅔 DATA (Errors): --------------


    #---------------- ㉧ LOCATORS: ----------------
    # -Buttons-
    @property
    def create_btn(self):
        return self.page.get_by_role("button", name="Create")

    # -Fields-
    @property
    def view_name_field(self):
        return self.page.locator('#name')


    # -View Types (radio buttons)-
    @property
    def include_a_global_view_type(self):
        return self.page.get_by_text('Include a global view')
    @property
    def list_view_type(self):
        return self.page.get_by_text('List View')
    @property
    def my_view_type(self):
        return self.page.get_by_text('My View')


    #==================================================== ✨HELPERS ====================================================
    """ Open <New View> page """
    def open(self, item_name: str):
        return self.open_page(self.endpoint(item_name))         # -→ <New View> page                                          http://localhost:8080/job/=ITEM_NAME=/newView