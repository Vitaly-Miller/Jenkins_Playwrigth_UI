"""
Create pipeline
TC_00_000_00
"""
from playwright.sync_api import expect
from data.generators import Fake
from pages.main.main_page import MainPage
from pages.main.items.new_item_page import NewItemPage
from func.api import API

#=======================================================================================================================
def test_create_pipeline(page, api_delete_all_jobs):  # + фикстура <delete_all_jobs> - удаляет ВСЕ jobs ПЕРЕД тестом     - (optional)
    #-------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    new_item_page = NewItemPage(page)

    #-------------- ⏎ DATA (input): --------------
    pipeline_name = Fake.pipeline_name

    #---------------- ▶︎ ACTIONS: -----------------
    main_page.open_page()                             # -→ <Main> page (Dashboard)                                       http://localhost:8080/
    new_item_page.new_item_btn.click()                # Click <New item> button -→ <New Item> page                       http://localhost:8080/view/all/newJob
    new_item_page.create_pipeline(pipeline_name)      # ✨Create Pipeline -→ <Configuration - General> page              http://localhost:8080/job/=PIPELINE_NAME=/configure
    new_item_page.logo_btn.click()                    # Click <Logo> button -→ <Main> page (Dashboard)                   http://localhost:8080/

    #--------------- 𝌮 VARIABLES: ----------------
    table_pipeline_name = main_page.table_item_name_link(pipeline_name)


    #------------- ✔︎ EXPECTATIONS: ---------------
    # Созданный job (item) появился в таблице на Dashboard
    expect(table_pipeline_name,
           f'❌Pipeline "{pipeline_name}" not found on the Dashboard able!').to_have_text(pipeline_name)

    #---------------- ⌫ CLEANUP: -----------------
    # (API) Delete job
    API.delete_job(pipeline_name)

#-----------------------------------------------------------------------------------------------------------------------
