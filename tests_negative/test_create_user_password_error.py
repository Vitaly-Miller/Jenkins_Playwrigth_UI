"""
Create user password error message
TC_00_000_00
"""
from pages.manage.create_user_page import CreateUserPage
from pages.manage.user_database_page import UserDatabasePage
from data.invalid_data import Invalid
from playwright.sync_api import expect

#=======================================================================================================================
def test_create_user_password_error_message(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    create_user_page = CreateUserPage(page)
    user_database_page = UserDatabasePage(page)

    #---------------- ▶︎ ACTIONS: -----------------
    user_database_page.open_page()                        # -→ <Jenkins’ own User Database> page (Table)                 http://localhost:8080/manage/securityRealm
    user_database_page.create_user_btn.click()            # Click <Create User> button -→ <Create User>  page            http://localhost:8080/manage/securityRealm/addUser
    create_user_page.fill_user_data_fields(               # ✨Fill with User Fake data (by default), but ....
        confirm_password=Invalid.CONFIRM_PASSWORD         # ... + ❌Incorrect confirm password (changes default value)
    )                                                     # -→ <Jenkins’ own User Database> page (Table)                 http://localhost:8080/manage/securityRealm

    #--------------- 𝌮 VARIABLES: ----------------
    message = create_user_page.password_error_msg
    message_list = message.all_text_contents()            # ['text_1', 'text_2']
    text_1 = message_list[0]
    text_2 = message_list[1]
    expected_text = CreateUserPage.PASSWORD_ERROR_MSG_TEXT


    #--------------- ✔ ASSERTIONS: --------------- (optional variants)
    # 1) Length of an error message is 2 objects in [list]
    assert len(message_list) == 2
    # 2) Error message has whole text
    assert message_list == expected_text
    # 3) text-1 = text-2
    assert text_1 == text_2
    # 4-5) Множество (отсутствие дубликатов)
    a = set(message_list)
    assert len(a) == 1
    assert a == {text_1}

    #------------- ✔︎ EXPECTATIONS: ---------------
    # 6) Error message text
    expect(message, '❌Wrong Password Error message!').to_have_text(expected_text)

#-----------------------------------------------------------------------------------------------------------------------