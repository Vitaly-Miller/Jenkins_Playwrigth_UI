"""
Create new View inside the Folder
TC_00.000.00
"""
from pages.main.items.new_item_page import NewItemPage
from pages.main.items.new_view_page import NewViewPage
from pages.main.items.view_page import ViewPage
from pages.main.main_page import MainPage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
def test_create_view_in_folder(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    new_item_page = NewItemPage(page)
    main_page = MainPage(page)
    item_page = NewItemPage(page)
    new_view_page = NewViewPage(page)
    view_page = ViewPage(page)

    #-------------- ⏎ DATA (input): --------------
    item_name = Fake.folder_name
    view_name = Fake.view_item_name

    #-------------- ◁ PRECONDITION: --------------
    # Create new folder -> Open folder
    new_item_page.open_page()                               # -→ <New Item> page                                         http://localhost:8080/view/all/newJob
    new_item_page.create_folder(item_name)                  # ✨Create new folder -→ <Configuration - General> page      http://localhost:8080/job/=ITEM_MANE=/configure
    main_page.logo_btn.click()                              # Click <Jenkins> logo -→ <Main> page (Dashboard)            http://localhost:8080/
    main_page.table_item_name_link(item_name).click()       # Click folder name -→ <Folder> page                         http://localhost:8080/job/=ITEM_NAME=/

    #---------------- ▶︎ ACTIONS: -----------------
    item_page.new_view_btn.click()                          # Click <New View> button -→ <New View> page                 http://localhost:8080/job/=ITEM_NAME=/newView
    new_view_page.view_name_field.fill(view_name)           # Fill View name field
    new_view_page.my_view_type.click()                      # Select <My View> type
    new_view_page.create_btn.click()                        # Click <Create> button -→ <View> page                       http://localhost:8080/job/=ITEM_NAME=/view/=VIEW_NAME=/

    #--------------- 𝌮 VARIABLES: ----------------
    expected_url = view_page.endpoint(item_name,  view_name)
    expected_title_text = view_page.title_text(item_name, view_name)
    expected_header_text = view_page.header_text(item_name)


    #------------- ✔︎ EXPECTATIONS: --------------
    # Page URL
    expect(page, f'❌Incorrect URL').to_have_url(expected_url)
    # Page Title text
    expect(page, f'❌Incorrect Title text').to_have_title(expected_title_text)
    # Page Header text
    expect(view_page.header, f'❌Incorrect Header text').to_have_text(expected_header_text)

    #---------------- ⌫ CLEANUP: -----------------
    # (API) Delete item (job)
    API.delete_item(item_name)

#-----------------------------------------------------------------------------------------------------------------------