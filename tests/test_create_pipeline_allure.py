"""
Created Pipeline is visible on Dashboard
TC_00_000_00
"""
import allure
from pages.main.main_page import MainPage
from pages.main.items.new_item_page import NewItemPage
from pages.main.items.item_configuration_general_page import ConfigurationGeneralPage
from data.generators import Fake
from playwright.sync_api import expect
from func.api import API

#=======================================================================================================================
@allure.epic('Jenkins')
@allure.story('New Item')
@allure.feature('Create Pipeline')
@allure.description('Created Pipeline is visible on Dashboard')
@allure.testcase('TC_00_000_00')
def test_create_pipeline(page, api_delete_all_jobs):  # + фикстура <delete_all_jobs> - удаляет ВСЕ jobs ПЕРЕД тестом     - (optional)
    #-------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)
    configuration_general_page = ConfigurationGeneralPage(page)

    #-------------- ⏎ DATA (input): --------------
    item_name = Fake.pipeline_name

    #---------------- ▶︎ ACTIONS: -----------------
    main_page.open_page()                             # -→ <Main> page (Dashboard)                                       http://localhost:8080/
    main_page.new_item_btn.click()                    # Click <New item> button -→ <New Item> page                       http://localhost:8080/view/all/newJob
    new_item_page.create_pipeline(item_name)          # ✨Create Pipeline -→ <Configuration - General> page              http://localhost:8080/job/=PIPELINE_NAME=/configure
    configuration_general_page.logo_btn.click()       # Click <Jenkins> logo -→ <Main> page (Dashboard)                  http://localhost:8080/

    #--------------- 𝌮 VARIABLES: ----------------
    table_item_name = main_page.table_item_name_link(item_name)

    #------------- ✔︎ EXPECTATIONS: ---------------
    # Созданный Item появился в таблице
    expect(table_item_name, f'❌Item "{item_name}" not found on the Dashboard able!').to_have_text(item_name)

    #---------------- ⌫ CLEANUP: -----------------
    # (API) Delete item (job)
    API.delete_item(item_name)

#-----------------------------------------------------------------------------------------------------------------------