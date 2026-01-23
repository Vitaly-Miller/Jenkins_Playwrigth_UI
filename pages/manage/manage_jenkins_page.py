"""
<Manage Jenkins> page
http://localhost:8080/manage/
"""
from pages.base_page import BasePage

#=======================================================================================================================
class ManageJenkinsPage(BasePage):
    #------------------ 𝌆 DATA: ------------------
    ENDPOINT = '/manage/'
    TITLE_TEXT = 'Manage Jenkins - Jenkins'
    HEADER_TEXT = 'Manage Jenkins'

    #---------------- ㉧ LOCATORS: ----------------


    #===================================================== ✨HELPERS ===================================================
    """ Open <Manage Jenkins> page """
    def open(self):
        self.open_page(self.ENDPOINT)                      # Open <Manage Jenkins> page                                  http://localhost:8080/manage