"""
Create item invalid name error
TC_00_000_00
"""
from data.invalid_data import Invalid
from pages.items.new_item_page import NewItemPage
from pages.main.main_page import MainPage
from playwright.sync_api import expect

#=======================================================================================================================
def test_create_item_invalid_name_error(page):
    # -------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)

    # -------------- ⏎ DATA (input): --------------
    invalid_item_name = Invalid.ITEM_NAME

    # ---------------- ▶︎ ACTIONS: -----------------
    main_page.open()                                                  # Open <Main> page (Dashboard)                     http://localhost:8080/
    main_page.new_item_btn.click()                                    # Click <New Item> button -→ <New Item> page       http://localhost:8080/view/all/newJob
    new_item_page.pipeline_link.click()                               # Select Pipeline type
    new_item_page.enter_item_name_field.fill(invalid_item_name)       # ❌Fill invalid item name

    # --------------- 𝌮 VARIABLES: ----------------
    error_msg = new_item_page.invalid_item_name_error_msg
    error_msg_text = new_item_page.INVALID_ITEM_NAME_ERROR_TEXT
    ok_btn = new_item_page.ok_btn
    text_color = new_item_page.ERROR_TEXT_COLOR_RED

    # ------------- ✔︎ EXPECTATIONS: ---------------
    # Error appears
    expect(error_msg, '❌Error message did NOT appear!').to_be_visible()
    # Error text content
    expect(error_msg, '❌Wrong error message text!').to_contain_text(error_msg_text)
    # Error text color (CSS)
    expect(error_msg, '❌Wrong error message text color!').to_have_css('color', text_color)
    # <OK> button is disable
    expect(ok_btn, '❌<OK> button is enable!').to_be_disabled()

#-----------------------------------------------------------------------------------------------------------------------