"""
Manage Jenkins button is clickable
TC_00_000_00
"""
from pages.main.main_page import MainPage
from pages.manage.manage_jenkins_page import ManageJenkinsPage
from func.api import API
from playwright.sync_api import expect

#=======================================================================================================================
def test_manage_jenkins_btn_is_clickable(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)
    manage_jenkins_page = ManageJenkinsPage(page)

    #---------------- ▶︎ ACTIONS: -----------------
    main_page.open_page()                                       # -→ <Main page> (Dashboard)                             http://localhost:8080/
    action = main_page.manage_jenkins_btn.click                 # 👈️click без () - ⚠️действие, а не результат
    response = API.api_by_status_code(                          # ✨ Моя функция перехвата API
        page,
        action,                                                 # Передаем action и status code302
        302,                                              # Ожидаемый status code при action
        True)                                         # API REPORT (print in console)

    #--------------- 𝌮 VARIABLES: ----------------
    title_text = manage_jenkins_page.TITLE_TEXT

    #------------- ✔︎ EXPECTATIONS: ---------------
    # New page URL
    expect(page, f'❌Incorrect <Manage Jenkins> page URL!').to_have_url('/manage/')
    # New page title text (⚠ NOT a Header ⚠)
    expect(page, f'❌Incorrect <Manage Jenkins> page Title text!').to_have_title(title_text)

    #---------------- ✔ ASSERTIONS: --------------
    # Status code
    assert response.status == 302, '❌Wrong status code!'

#-----------------------------------------------------------------------------------------------------------------------