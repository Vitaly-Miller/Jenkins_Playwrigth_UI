"""
Rename folder
Page Object Model (POM)
TC_00.000.00
"""
from pages.items.item_page import ItemPage
from pages.main.main_page import MainPage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
def test_rename_folder(page):
    # --------------- ⿴ PAGE OBJECTS: ---------------
    main_page = MainPage(page)
    item_page = ItemPage(page)

    # --------------- ⏎ DATA (input): ----------------
    item_name = Fake.item_name                              # Generate fake folder name
    item_name_new = f'New_{Fake.item_name}'                 # NEW folder name

    # ---------------- ◁ PRECONDITION: ---------------
    API.create_folder(item_name)                            # Create folder (API)

    # ----------------- ▶︎ ACTIONS: ------------------
    main_page.open()                                        # Open <Main page>                                           http://localhost:8080/
    main_page.table_item_name_link(item_name).click()       # Click on folder name -→ open folder page                   http://localhost:8080/job/=ITEM_NAME=/
    main_page.rename_link.click()                           # Click <Rename> link -→ open <Rename> page                  http://localhost:8080/job/=ITEM_NAME=/confirm-rename
    item_page.new_name_field.clear()                        # Clear an old folder name
    item_page.new_name_field.fill(item_name_new)            # Enter a new name
    item_page.rename_button.click()                         # Click <Rename> button -→ open folder page                  http://localhost:8080/job/=NEW_ITEM_NAME=/

    # ---------------- 𝌮 VARIABLES: -----------------
    item_page_header = item_page.header(item_name_new)

    # --------------- ✔︎ EXPECTATIONS: ---------------
    # An item page header is visible
    expect(item_page_header, f'❌Item new name is NOT visible!').to_be_visible()
    # An item page header has a correct New folder name
    expect(item_page_header, f'❌Wrong item new name!').to_have_text(item_name_new)

    # ------------------ ⌫ CLEANUP: ------------------
    API.delete_item(item_name_new)                         # Delete folder after test (API)

#-----------------------------------------------------------------------------------------------------------------------