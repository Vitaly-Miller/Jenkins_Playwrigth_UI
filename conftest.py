"""
Pytest fixtures
"""
import pytest
from playwright.sync_api import Playwright, ViewportSize
from data.base_data import Base
from pages.main.login_page import LoginPage
from func.api import API

#===================================================== Playwright ======================================================
""" Page + Storage State 🗄️ """
@pytest.fixture
def page(playwright: Playwright, storage_state):            # User Log in + фикстура storage_state
    browser = playwright.chromium.launch(                   # Запуск движка браузера с параметрами:
        channel='chromium',                                 # - UI оболочка: 'chromium', 'chrome', 'opera'
        headless=False,                                     # - False → показывать браузер
        slow_mo=500                                         # - Action Delay (ms)
    )
    context = browser.new_context(                          # Создание браузерного окружения:
        locale="en-US",                                     # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200),     # - Screen size
        base_url=Base.URL,                                  # - Base URL (from data/base_data.py)
        storage_state=storage_state                         # - storage_state 🗄️- Авторизация (cookies + localStorage)

    )
    #context.add_cookies(cookies)                           # 👈cookies 🍪(НЕ использую. Использую - storage_state ⬆︎)
    page = context.new_page()                               # Создание вкладки (страницы)
    page.set_default_timeout(5_000)                         # Fail default timeout (ms)
    yield page                                              # Возвращает объект Page в тест
    context.close()
    browser.close()

#------------------------------------------------------
""" GUEST Page (БЕЗ storage_state) """
@pytest.fixture
def page_guest(playwright: Playwright):                     # Чистый (без доп. фикстур)
    """
    ⭐️Лайфхак для Теста ⭐
    ----------------------
    def test_1(page_guest)
    page = page_guest ✨
    page.locator().click()
    ----------------------
    """ # <- ✨                                             # <- см. Лайфхак ✨
    browser = playwright.chromium.launch(                   # Запуск движка браузера с параметрами:
        channel='chromium',                                 # - UI оболочка: 'chromium', 'chrome', 'opera'
        headless=False,                                     # - False = показывать браузер
        slow_mo=500                                         # - Action Delay (ms)
    )
    context = browser.new_context(                          # Создание браузерного окружения:
        locale='en-US',                                     # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200),     # - Screen size
        base_url=Base.URL                                   # - Base URL (from data/base_data.py)
    )
    page = context.new_page()                               # Создание вкладки (страницы)
    page.set_default_timeout(5_000)                         # Fail default timeout (ms)
    yield page                                              # Возвращает объект Page в тест
    context.close()
    browser.close()


#-----------------------------------------------------------------------------------------------------------------------
""" Storage State 🗄 """  # (шире, чем Cookies)
"""
-----------------------------------------------------------
1) Залогинил User
2) Редирект на Main page
3) Сохранил Storage State на всю сессию
4) Закрылся
5) -> далее логику выполняет обычный .page с этой фикстурой
-----------------------------------------------------------
"""
@pytest.fixture(scope='session')
def storage_state(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(base_url=Base.URL)
    page = context.new_page()
    LoginPage(page).user_log_in()                          # ✨User Authorization (helper)
    yield context.storage_state()
    context.close()
    browser.close()

#-------------------------------------
""" Cookies 🍪"""  # (⚠️️НЕ использую)
@pytest.fixture(scope='session')
def cookies(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(base_url=Base.URL)
    page = context.new_page()
    LoginPage(page).user_log_in()                          # ✨User Authorization (helper)
    yield context.cookies()
    context.close()
    browser.close()


#================================================ API-fixtures (Pre-test) ==============================================
# ------------ Create items ------------
""" Create Pipeline """
@pytest.fixture
def api_create_pipeline():
    API.create_pipeline()

""" Create Freestyle project """
@pytest.fixture
def api_create_freestyle_project():
    API.create_freestyle_project()

""" Create Multi-configuration project """
@pytest.fixture
def api_create_multi_configuration_project():
    API.create_multi_configuration_project()

""" Create Folder """
@pytest.fixture
def api_create_folder():
    API.create_pipeline()

# ------------- Delete items -------------
""" Delete ALL items (jobs) """
@pytest.fixture
def api_delete_all_items():
    API.delete_all_items()
#-----------------------------------------------------------------------------------------------------------------------