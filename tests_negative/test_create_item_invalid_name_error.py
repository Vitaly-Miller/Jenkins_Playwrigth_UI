"""
Create item invalid name error
"""
from playwright.sync_api import expect
from pages.main.items.new_item_page import NewItemPage
from pages.main.main_page import MainPage

#=======================================================================================================================
def test_create_item_invalid_name_error(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)

    #-------------- ⏎ DATA (input): --------------
    invalid_item_name = 'Invalid#Name'                            # <#> - non accessible symbol

    #---------------- ▶︎ ACTIONS: -----------------
    main_page.open_page()                                         # -→ <Main> page (Dashboard)                           http://localhost:8080/
    main_page.new_item_btn.click()                                # Click <New Item> button -→ <New Item> page           http://localhost:8080/view/all/newJob
    new_item_page.enter_item_name_field.fill(invalid_item_name)   # ❌ Fill invalid item name

    #--------------- 𝌮 VARIABLES: ----------------
    error_msg = new_item_page.invalid_item_name_error_msg
    error_msg_text = new_item_page.INVALID_ITEM_NAME_ERROR_MSG_TEXT
    ok_btn = new_item_page.ok_btn
    text_red_color = new_item_page.ERROR_MSG_TEXT_COLOR


    #------------- ✔︎ EXPECTATIONS: ---------------
    # Error appears
    expect(error_msg, '❌Error message did NOT appear!').to_be_visible()
    # Error text content
    expect(error_msg, '❌Wrong error message text!').to_contain_text(error_msg_text)
    # Error text color is red (CSS)
    expect(error_msg, '❌Wrong error message text color!').to_have_css('color', text_red_color)
    # <OK> button is disable
    expect(ok_btn, '❌<OK> button is enable!').to_be_disabled()

#-----------------------------------------------------------------------------------------------------------------------