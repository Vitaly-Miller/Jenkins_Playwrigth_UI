"""
Create User
TC_00_000_00
"""
from pages.manage.create_user_page import CreateUserPage
from pages.manage.user_database_page import UserDatabasePage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
def test_create_user(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    user_database_page = UserDatabasePage(page)
    create_user_page = CreateUserPage(page)

    #-------------- ⏎ DATA (input): --------------
    username = Fake.username
    user_full_name = Fake.user_full_name

    #---------------- ▶︎ ACTIONS: -----------------
    user_database_page.open()                        # -> <Jenkins’ own User Database> page (Table)                      http://localhost:8080/manage/securityRealm
    user_database_page.create_user_btn.click()       # Click <Create User> button> -→ <Create User> page                 http://localhost:8080/manage/securityRealm/addUser
    create_user_page.fill_user_data_fields()         # ✨Fill User data fields -→ <Jenkins’ own User Database> page      http://localhost:8080/manage/securityRealm

    # --------------- 𝌮 VARIABLES: ---------------
    table_user_id = user_database_page.table_user_id(username)
    table_user_name = user_database_page.table_user_name(user_full_name)


    #------------- ✔︎ EXPECTATIONS: ---------------
    # Created <Username> появился в таблице (User ID)
    expect(table_user_id, f'❌User "{username}" not found!').to_have_text(username)
    # Created <User Name> появился в таблице (Full Name)
    expect(table_user_name, f'❌Incorrect User Full Name!').to_have_text(user_full_name)

    #---------------- ⌫ CLEANUP: -----------------
    # Delete created User
    user_database_page.delete_user(username)
    # (API) Delete created User (optional)
    API.delete_user(username)


#-----------------------------------------------------------------------------------------------------------------------