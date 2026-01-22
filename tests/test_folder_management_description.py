"""
Folder Management > Add a Job Description > Verify Add folder description #134
TC_00_000_00
"""
from pages.main.main_page import MainPage
from playwright.sync_api import expect

#=======================================================================================================================
def test_fill_description(page):
    #-------------- ⧈ PAGE OBJECTS: --------------
    main_page = MainPage(page)

    #-------------- ⏎ DATA (input): --------------
    description_text = 'My test description text - 1234567890!'

    #---------------- ▶︎ ACTIONS: -----------------
    main_page.open()                                            # Open <Main> page (Dashboard)                           http://localhost:8080/
    main_page.add_description(description_text)                 # ✨Open description form and fill text

    #------------- ✔︎ EXPECTATIONS: ---------------
    # Текст появился в заголовке страницы
    expect(main_page.description_header, f'❌Wrong description header!').to_have_text(description_text)

    #---------------- ⌫ CLEANUP: -----------------
    # Clear description field
    main_page.clear_description()

#-----------------------------------------------------------------------------------------------------------------------