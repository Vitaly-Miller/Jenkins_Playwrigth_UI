"""
Rename folder
NON Page Object Model (NON POM)
TC_00.000.00
"""
from playwright.sync_api import Page, expect
import random
import requests

#=======================================================================================================================
def test_rename_folder_non_pom(page: Page):
    # ==================== 𝌆 Base DATA =====================
    base_url = 'http://localhost:8080'
    login_page_endpoint = '/login'
    create_item_endpoint = '/view/all/createItem'
    delete_item_endpoint = lambda x: f'/job/{x}/doDelete'
    folder_api_mode = 'com.cloudbees.hudson.plugins.folder.Folder'

    # ==================== ◁ PRECONDITION ===================
    # ----- Authorization (Log in) -----
    page.goto(f'{base_url}{login_page_endpoint}')             # Open <Login> page                                        http://localhost:8080/login

    # Page element locators
    admin_username_field = page.locator('#j_username')
    admin_password_field = page.locator('#j_password')
    sign_in_btn = page.locator('button[name="Submit"]')

    # ⚠️Admin data (credentials)
    admin_username = 'Vitaly_Miller'                          # Admin username
    admin_password = 'test_Pass_123'                          # Admin password
    admin_api_token = '11baf1d6f2b5f2a3d4eaa977191ae9117e'    # Admin API token

    # Fill page fields with admin credentials:
    admin_username_field.fill(admin_username)                 # Enter Admin username
    admin_password_field.fill(admin_password)                 # Enter Admin password
    sign_in_btn.click()                                       # Click <Sign in> button -→ <Main> page (Dashboard)        http://localhost:8080/

    # -------- Create folder --------
    # Folder name generator
    random_num = random.randint(10, 99)                 # Random numbers generator (10-99)
    item_name = f'Folder_name-{random_num}'                   # Generate fake folder name
    item_name_new = f'NEW_Folder_name-{random_num}'           # NEW folder name

    # Create folder (API)
    requests.post(
        url=f'{base_url}{create_item_endpoint}',
        auth=(admin_username, admin_api_token),
        data={
            'name': item_name,
            'mode': folder_api_mode
        }
    )
    # ====================== ▶︎ ACTIONS ====================
    # Page element locators
    folder_name_link = page.locator(f'span:has-text("{item_name}")')
    rename_link = page.get_by_role('link', name='Rename')
    input_field = page.locator('input[name="newName"]')
    rename_btn = page.get_by_role('button', name='Rename')

    # Actions
    page.goto('http://localhost:8080')                        # Open <Main page>
    folder_name_link.click()                                  # Click on folder name -→ open folder page                 http://localhost:8080/job/=ITEM_NAME=/
    rename_link.click()                                       # Click <Rename> link -→ open <Rename> page                http://localhost:8080/job/=ITEM_NAME=/confirm-rename
    input_field.clear()                                       # Clear an old folder name
    input_field.fill(item_name_new)                           # Enter a new name
    rename_btn.click()                                        # Click <Rename> button -→ open folder page                http://localhost:8080/job/=NEW_ITEM_NAME=/

    # ================== ✔︎ EXPECTATIONS: ===================
    # Page element locators
    item_page_header = page.get_by_role('heading', name=item_name_new)

    # An item page header is visible
    expect(item_page_header, f'❌Item new name is NOT visible!').to_be_visible()

    # An item page header has a correct New folder name
    expect(item_page_header, f'❌Wrong item new name!').to_have_text(item_name_new)

    # ===================== ⌫ CLEANUP: ======================
    # Delete folder after test (API)
    requests.post(
        url=f'{base_url}{delete_item_endpoint(item_name_new)}',
        auth=(admin_username, admin_api_token)
    )

#-----------------------------------------------------------------------------------------------------------------------