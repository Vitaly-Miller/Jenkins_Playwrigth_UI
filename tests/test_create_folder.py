"""
Folder Configuration > Display Name and Description
TC_00_000_00
"""
from pages.main.main_page import MainPage
from pages.items.new_item_page import NewItemPage
from pages.items.item_configuration_general_page import ConfigurationGeneralPage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
def test_create_new_folder(page):
    # ---- ⧈ PAGE OBJECTS ----
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)
    configuration_general_page = ConfigurationGeneralPage(page)

    # ---- ⏎ DATA (input) ----
    item_name = Fake.item_name
    display_name = f'***{item_name}***'                         # User-friendly name (for table display)

    # ---- ▶︎ ACTIONS ----
    main_page.open()                                            # Open <Main> page (Dashboard)                           http://localhost:8080/
    main_page.new_item_link.click()                             # Click <New Item> button -→ <New Item> page             http://localhost:8080/view/all/newJob
    new_item_page.create_folder(item_name)                      # ✨Create Folder -→ <Configuration - General> page      http://localhost:8080/job/=FOLDER_NAME=/configure
    configuration_general_page.fill_display_name(display_name)  # ✨Fill <Display Name> field (User-friendly)
    configuration_general_page.logo_btn.click()                 # Click <Jenkins> logo -→ <Main> page (Dashboard)        http://localhost:8080/

    # ---- 𝌮 VARIABLES ----
    table_display_name = main_page.table_item_name_link(display_name)

    # ---- ✔︎ EXPECTATIONS ----
    # Созданный Item c Display name появился в таблице на Dashboard
    expect(table_display_name,
           f'❌Display name "{display_name}" not found on the Dashboard table!').to_have_text(display_name)

    # ---- ⌫ CLEANUP ----
    # (API) Delete item (job)
    API.delete_item(item_name)


#-----------------------------------------------------------------------------------------------------------------------