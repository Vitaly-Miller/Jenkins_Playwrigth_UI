"""
User > Delete > Cancel the Delete button from the drop-down menu
TC_00_000_00
"""
from pages.manage.create_user_page import CreateUserPage
from pages.manage.user_database_page import UserDatabasePage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
def test_cancel_delete_user(page):
    # -------------- ⧈ PAGE OBJECTS: -------------
    user_database_page = UserDatabasePage(page)
    create_user_page = CreateUserPage(page)

    # -------------- ◁ PRECONDITION: -------------
    # Create User (Fake data)
    user_database_page.open()                        # Open <Jenkins’ own User Database> page (Table)                    http://localhost:8080/manage/securityRealm
    user_database_page.create_user_btn.click()       # Click <Create User> button> -→ <Create User> page                 http://localhost:8080/manage/securityRealm/addUser
    create_user_page.fill_user_data_fields()         # ✨Fill User data fields -→ <Jenkins’ own User Database> page      http://localhost:8080/manage/securityRealm

    # -------------- ⏎ DATA (input): -------------
    username = Fake.username

    # ---------------- ▶︎ ACTIONS: ----------------
    user_database_page.user_dropdown_menu_chevron(username).click()      # Open User dropdown menu
    user_database_page.dropdown_menu_delete_btn(username).click()        # Click <Delete> button
    user_database_page.delete_cancel_btn.click()                         # Click <Cancel> button

    # --------------- 𝌮 VARIABLES: ---------------
    table_user_id = user_database_page.table_user_id(username)

    # -------------- ✔︎ EXPECTATIONS: -------------
    # Username остался в таблице Database (User ID)
    expect(table_user_id, f'❌User "{username}" not found!').to_have_text(username)

    # ---------------- ⌫ CLEANUP: ----------------
    # (API) Delete User
    API.delete_user(username)




#-----------------------------------------------------------------------------------------------------------------------