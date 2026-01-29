"""
API Functions and Helpers
"""
from data.base_data import Base
import requests
from data.generators import Fake
from formatting.console_report import APIreport

#=======================================================================================================================
class APIintercept:
    # ---------------- API interception  -----------------
    # Intercept by Status code
    """
        Ожидание Request + Перехват Response <status code>
        ➡︎ .expect_response() - Playwright говорит браузеру:
             1. «Когда в ближайшее время произойдёт сетевой ЗАПРОС — перехвати его».
             2. «И как только придёт НУЖНЫЙ ответ → положи его в переменную response_info».

        ➡︎ lambda r: r.status == 200
             1) Перехвати КАЖДЫЙ сетевой ОТВЕТ
             2) Подставь его в lambda как аргумент <r>
             3) Проверь условие (r.status == 200)
             4) Как только условие вернуло True — это "наш" <r> → положи его в переменную response_info
    """
    @staticmethod
    def by_status_code(page, action, code: int, api_report: bool = False):        # NO API report by default
        with page.expect_response(lambda r: r.status == code) as response_info:   # Перехватить Response с определенным <status code>
            action()                                                # 👈 Перехватываемый action
            response = response_info.value                          # Внутренний контейнер => в рабочий Response
            if api_report:
                API.report(response)                                # API REPORT в консоль if True (optional)
        return response

    # Intercept by URL
    @staticmethod
    def by_url(page, action, url: str, api_report: bool = False):   # NO API report by default
        with page.expect_response(url) as response_info:            # Перехватить Response c URL
            action()                                                # 👈 Перехватываемый action
            response = response_info.value                          # Внутренний контейнер => в рабочий Response
            if api_report:
                API.report(response)                                # API REPORT в консоль if True (optional)
        return response


class API:
    # ======================= Users =======================
    # -------------------- Create user --------------------
    # Create user
    @staticmethod
    def create_user(
            username: str = Fake.username,
            password: str = Fake.user_password,
            full_name: str = Fake.user_full_name,
            email: str = Fake.user_email,
            api_report: bool = False
    ):
        requests.post(
            url=f'{Base.URL}{Base.CREATE_USER_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'username': username,
                'password1': password,
                'password2': password,
                'fullname': full_name,
                'email': email
            }
        )

    # -------------------- Delete user --------------------
    # Delete user by username
    @staticmethod
    def delete_user(username: str):
        requests.post(
            url=f'{Base.URL}{Base.DELETE_USER_ENDPOINT(username)}',
            auth=(Base.USERNAME, Base.API_TOKEN)
        )

    # ==================== Items (Jobs) ===================
    # -------------- Create item (All-in-One) -------------
    @staticmethod
    def create_item(
            item_type: str = Fake.random_item_type,
            item_name: str = Fake.item_name
    ):
        if item_type == 'pipeline':
            item_mode = Base.PIPELINE_API_MODE
        elif item_type == 'freestyle_project':
            item_mode = Base.FREESTYLE_PROJECT_API_MODE
        elif item_type == 'multi_configuration_project':
            item_mode = Base.MULTI_CONFIGURATION_PROJECT_API_MODE
        elif item_type == 'folder':
            item_mode = Base.FOLDER_API_MODE
        else:
            raise ValueError(Base.MODE_ERROR)

        requests.post(
            url=f'{Base.URL}{Base.CREATE_ITEM_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'name': item_name,
                'mode': item_mode
            }
        )

    # -------------- Create item (by Type) --------------
    # Create Pipeline
    @staticmethod
    def create_pipeline(item_name: str = Fake.item_name):
        requests.post(
            url=f'{Base.URL}{Base.CREATE_ITEM_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'name': item_name,
                'mode': Base.PIPELINE_API_MODE
            }
        )

    # Create Freestyle project
    @staticmethod
    def create_freestyle_project(item_name: str = Fake.item_name):
        requests.post(
            url=f'{Base.URL}{Base.CREATE_ITEM_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'name': item_name,
                'mode': Base.FREESTYLE_PROJECT_API_MODE
            }
        )

    # Create Multi-configuration project
    @staticmethod
    def create_multi_configuration_project(item_name: str = Fake.item_name):
        requests.post(
            url=f'{Base.URL}{Base.CREATE_ITEM_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'name': item_name,
                'mode': Base.MULTI_CONFIGURATION_PROJECT_API_MODE
            }
        )

    # Create Folder
    @staticmethod
    def create_folder(item_name: str = Fake.item_name):
        requests.post(
            url=f'{Base.URL}{Base.CREATE_ITEM_ENDPOINT}',
            auth=(Base.USERNAME, Base.API_TOKEN),
            data={
                'name': item_name,
                'mode': Base.FOLDER_API_MODE
            }
        )

    # ------------------ Delete items -----------------
    # Delete item (job) by nane
    @staticmethod
    def delete_item(item_name: str):
        requests.post(
            url=f'{Base.URL}{Base.DELETE_ITEM_ENDPOINT(item_name)}',
            auth=(Base.USERNAME, Base.API_TOKEN))


    # Delete ALL items (jobs)
    @staticmethod
    def delete_all_items():
        # Получение [списка] всех jobs
        item_list = requests.get(
            url=f'{Base.URL}/api/json',
            auth=(Base.USERNAME, Base.API_TOKEN)
        ).json()['jobs']
        # Удаление каждого job по имени (цикл for)
        for job in item_list:
            item_name = job['name']
            requests.post(
                url=f'{Base.URL}{Base.DELETE_ITEM_ENDPOINT(item_name)}',
                auth=(Base.USERNAME, Base.API_TOKEN))





    #================ API REPORT (8-in-1) ================
    """ ⚠️USE with .expect_response() only """
    @staticmethod
    def report(response):
        APIreport.title()
        APIreport.url(response)
        APIreport.method(response)
        APIreport.status_code(response)
        APIreport.request_body(response)
        APIreport.response_body(response)
        APIreport.request_headers(response)
        APIreport.response_headers(response)