"""
Freestyle project description
TC_00_000_00
"""
from playwright.sync_api import expect
from data.generators import Fake
from pages.items.item_configuration_general_page import ConfigurationGeneralPage
from pages.items.item_page import ItemPage
from pages.items.new_item_page import NewItemPage
from pages.main.main_page import MainPage
from func.api import API

#=======================================================================================================================
def test_freestyle_project_description(page):
    # -------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)
    configuration_general_page = ConfigurationGeneralPage(page)
    item_page = ItemPage(page)

    # -------------- ⏎ DATA (input): --------------
    item_name = Fake.item_name
    description_text = 'My test description text - 1234567890!'
    new_description_text = 'My NEW test description text - 👀✅❌✔️😀👍!'

    # ---------------- ▶︎ ACTIONS: ----------------
    main_page.open()                                                 # Open <Main> page                                  http://localhost:8080/
    main_page.new_item_link.click()                                   # Click <New Item> button -→ <New Item> page       http://localhost:8080/view/all/newJob
    new_item_page.create_freestyle_project(item_name)                # ✨Create a Freestyle project -→ Config  page      http://localhost:8080/job/=FREESTYLE_PROJECT_NAME=/configure
    configuration_general_page.save_btn.click()                      # Click <Save> button -→ <Item> page                http://localhost:8080/job/=FREESTYLE_PROJECT_NAME=
    new_item_page.add_description(description_text)                  # ✨Add Description -→ <Item> page                  http://localhost:8080/job/=FREESTYLE_PROJECT_NAME=
    item_page.edit_description(new_description_text)                 # ✨Edit Description -→ <Item> page                 http://localhost:8080/job/=FREESTYLE_PROJECT_NAME=

    # --------------- 𝌮 VARIABLES: ---------------
    description_header = item_page.description_header
    edit_description_btn = item_page.edit_description_btn
    expected_edit_description_btn_text = item_page.EDIT_DESCRIPTION_BTN_TEXT

    # ------------- ✔︎ EXPECTATIONS: --------------
    # New description is displayed below the freestyle project name
    expect(description_header,
           f'❌Incorrect Description text!').to_have_text(new_description_text)
    # <Edit description> button has correct text
    expect(edit_description_btn,
           f'❌Incorrect <Edit description> button label!').to_have_text(expected_edit_description_btn_text)

    # ---------------- ⌫ CLEANUP: -----------------
    # (API) Delete job
    API.delete_item(item_name)

#-----------------------------------------------------------------------------------------------------------------------