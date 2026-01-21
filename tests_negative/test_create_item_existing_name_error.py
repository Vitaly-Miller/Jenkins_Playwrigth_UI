"""
Existing item name error
TC_00_000_00
"""
from pages.main.main_page import MainPage
from pages.main.items.new_item_page import NewItemPage
from func.api import API
from playwright.sync_api import expect

#=======================================================================================================================
def test_create_item_existing_name_error(page):
    #-------------- ⧈ PAGE OBJECTS: ---------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)

    #-------------- ⏎ DATA (input): ---------------
    item_name = 'Test_Item_Name'

    #-------------- ◁ PRECONDITION: ---------------
    # API Create Freestyle project
    API.create_freestyle_project(item_name)

    # ---------------- ▶︎ ACTIONS: -----------------
    main_page.open()                                                  # Open <Main> page (Dashboard)                     http://localhost:8080/
    main_page.new_item_btn.click()                                    # Click <New item> button -→ <New Item> page       http://localhost:8080/view/all/newJob
    new_item_page.freestyle_project_link.click()                      # Select Freestyle project type
    new_item_page.enter_item_name_field.fill(item_name)               # ❌Fill existing item name

    # --------------- 𝌮 VARIABLES: ----------------
    error_msg = new_item_page.invalid_item_name_error_msg
    error_msg_text = new_item_page.EXIST_ITEM_MANE_ERROR_TEXT
    ok_btn = new_item_page.ok_btn
    text_color = new_item_page.ERROR_TEXT_COLOR_RED

    #-------------- ✔︎ EXPECTATIONS: ---------------
    # Error appears
    expect(error_msg, '❌Error message did NOT appear!').to_be_visible()
    # Error text content
    expect(error_msg, '❌Wrong error message text!').to_contain_text(error_msg_text)
    # Error text color (CSS)
    expect(error_msg, '❌Wrong error message text color!').to_have_css('color', text_color)
    # <OK> button is disable
    expect(ok_btn, '❌<OK> button is enable!').to_be_disabled()

    #----------------- ⌫ CLEANUP: -----------------
    # (API) Delete all items
    API.delete_all_items()

#-----------------------------------------------------------------------------------------------------------------------