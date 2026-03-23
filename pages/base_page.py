"""
BASE page
(Common elements)
"""
from playwright.sync_api import Page

#=======================================================================================================================
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # -------------------------------------------------- 𝌆 DATA --------------------------------------------------------
    EDIT_DESCRIPTION_BTN_TEXT = 'Edit description'
    SAVE_DESCRIPTION_BTN_TEXT = 'Save'
    CANCEL_DESCRIPTION_BTN_TEXT = 'Cancel'

    # ------------------------------------------------ ㉧ LOCATORS ------------------------------------------------------
    # ---- Buttons -----
    @property
    def logo_btn(self):
        return self.page.locator('.app-jenkins-logo')                            # -→ <Main> page (Dashboard)            http://localhost:8080/

    @property
    def manage_jenkins_btn(self):
        return self.page.get_by_role('link', name='Manage Jenkins')         # -→ <Manage Jenkins> page              http://localhost:8080/manage

    # ---- Tab bar -----
    @property
    def all_btn(self):
        return self.page.get_by_role('link', name='All')                    # -→ <Main> page (Dashboard)            http://localhost:8080/

    @property
    def new_view_btn(self):
        return self.page.get_by_role('link', name='New View')               # -→ <New View> page                    http://localhost:8080/newView

    # ---- ⬆ ︎Nav bar ----
    @property
    def nav_bar(self):
        return self.page.locator('#page-header')

    @property
    def breadcrumb_bar(self):
        return self.page.locator('#breadcrumbBar')

    @property
    def breadcrumbs(self):
        return self.page.locator('li.jenkins-breadcrumbs__list-item')

    # ---- ⬅︎ Left side panel ----
    @property
    def left_panel(self):
        return self.page.locator('#side-panel')

    @property
    def status_link(self):
        return self.page.get_by_role('link', name='Status', exact=True)

    @property
    def changes_link(self):
        return self.page.get_by_role('link', name='Changes')

    @property
    def configure_link(self):
        return self.page.get_by_role('link', name='Configure')

    @property
    def new_item_link(self):
        return self.page.get_by_role('link', name='New Item')

    @property
    def delete_item_link(self):
        return self.page.locator('[class="icon-edit-delete icon-md"]')             # 🗑️ (by icon)

    @property
    def delete_item_confirm_yes_btn(self):
        return self.page.locator('button[data-id="ok"]')

    @property
    def build_history_link(self):
        return self.page.get_by_role('link', name='Build History')


    # ---- Rename -----
    @property
    def rename_link(self):
        return self.page.get_by_role('link', name='Rename')

    @property
    def new_name_field(self):
        return self.page.locator('input[name="newName"]')

    @property
    def rename_button(self):
        return self.page.get_by_role('button', name="Rename")

    @property
    def credentials_link(self):
        return self.page.get_by_role('link', name='Credentials')

    @property
    def move_link(self):
        return self.page.get_by_role('link', name='Move')

    @property
    def stages_link(self):
        return self.page.get_by_role('link', name='Stages')

    @property
    def build_link(self):
        return self.page.get_by_role('link', name='Build Now')

    @property
    def build_executor_status_link(self):
        return self.page.get_by_role('link', name='Build Executor Status', exact=True)

    @property
    def pipeline_syntax_link(self):
        return self.page.get_by_role('link', name='Pipeline Syntax')


    # ---- ⧈ Main panel (center) -----
    @property
    def main_panel(self):
        return self.page.locator('#main-panel')


    # ---- ⬇︎ Footer panel -----
    @property
    def footer(self):
        return self.page.locator('#footer')


    # ---- Description ----
    @property
    def add_description_btn(self):
        return self.page.locator('#description-link')

    @property
    def edit_description_btn(self):
        return self.page.get_by_role('link', name='Edit description')

    @property
    def description_field(self):
        return self.page.locator('textarea[name="description"]')

    @property
    def save_description_btn(self):
        return self.page.get_by_role('button', name='Save')

    @property
    def cancel_description_btn(self):
        return self.page.get_by_role('button', name='Cancel')

    @property
    def description_header(self):
        return self.page.locator('#description-content')



    #================================================== ✨HELPERS ======================================================
    # BASE OPEN PAGE
    def open_page(self, endpoint: str):
        self.page.goto(endpoint)

    # ---- Description ----
    # Add description
    def add_description(self, text: str):
        self.add_description_btn.click()                           # Open description form
        self.description_field.fill(text)                          # Fill text
        self.save_description_btn.click()                          # Click Save button (Save description)

    # Edit description
    def edit_description(self, text: str):
        self.edit_description_btn.click()                          # Open description form
        self.description_field.fill(text)                          # Fill text                                           (⚠ Предварительная отчистка поля не требуется)
        self.save_description_btn.click()                          # Click Save button (Save description)

    # Clear description
    def clear_description(self):
        self.add_description_btn.click()                           # Open description filling form
        self.description_field.clear()                             # Clear description field
        self.save_description_btn.click()                          # Click Save button (Save description)