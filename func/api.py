"""
API
"""
import json
from data.base_data import Base
import requests

#=======================================================================================================================
class API:
    #------------------- Delete user ---------------------
    @staticmethod
    def delete_user(username: str):
        requests.post(
            url=f"{Base.URL}/user/{username}/doDelete",
            auth=(Base.USERNAME, Base.API_TOKEN))


    #------------------ Delete job (item) ----------------
    @staticmethod
    def delete_job(job_name: str):
        requests.post(
            url=f"{Base.URL}/job/{job_name}/doDelete",
            auth=(Base.USERNAME, Base.API_TOKEN))


    #--------------- Delete ALL jobs (items) -------------
    @staticmethod
    def delete_all_jobs():
        # Получение [списка] всех jobs
        jobs_lst = requests.get(
            url=f'{Base.URL}/api/json',
            auth=(Base.USERNAME, Base.API_TOKEN)
        ).json()['jobs']
        # Удаление каждого job по имени (цикл for)
        for job in jobs_lst:
            job_name = job['name']
            requests.post(
                url=f'{Base.URL}/job/{job_name}/doDelete',
                auth=(Base.USERNAME, Base.API_TOKEN))

    #---------- API перехват (.expect_response()) ----------
    # by Status code
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
    def api_by_status_code(
            page,
            action,
            code: int,
            api_report: bool = False
    ):
        with page.expect_response(lambda r: r.status == code) as response_info:  # Перехватить Response с определенным <status code>
            action()                                                             # 👈 Перехватываемый action
            response = response_info.value                                       # Внутренний объект-контейнер => в рабочий Response
            if api_report:
                API.api_report(response)                                         # API REPORT в консоль if True (optional)
        return response

    # by URL
    @staticmethod
    def api_by_url(
            page,
            action,
            url: str,
            api_report: bool = False
    ):
        with page.expect_response(url) as response_info:           # Перехватить Response c URL
            action()                                               # 👈 Перехватываемый action
            response = response_info.value                         # Внутренний объект-контейнер => в рабочий Response
            if api_report:
                API.api_report(response)                           # API REPORT в консоль if True (optional)
        return response


    #--------------------- API Details --------------------
    # Title
    @staticmethod
    def api_title():
        print(f'\n\n🅰🅿︎🅸 🆁🅴🅿︎🅾🆁🆃')

    # URL
    @staticmethod
    def api_url(response):
        print(f'URL:\t\t {response.url}')

    # Method
    @staticmethod
    def api_method(response):
        print(f'METHOD:\t\t {response.request.method}')

    # Status code
    @staticmethod
    def api_status_code(response):
        print(f'STATUS CODE: {response.status}')

    # Request headers
    @staticmethod
    def api_request_headers(response):
        obj = dict(response.request.headers)
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print('\n--- REQUEST HEADERS ---')
        print(obj_json)

    # Request body
    @staticmethod
    def api_request_body(response):
        print('\n--- REQUEST BODY ---')
        if response.request.post_data:
            try:
                obj = json.loads(response.request.post_data)
                obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
                print(obj_json)
            except Exception:
                print(response.request.post_data)
        else:
            print('\t<None>')

    # Response headers
    @staticmethod
    def api_response_headers(response):
        obj = dict(response.headers)
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print('\n--- RESPONSE HEADERS ---')
        print(obj_json)

    # Response body
    @staticmethod
    def api_response_body(response):
        print('\n--- RESPONSE BODY ---')
        content_type = response.headers.get('content-type', '')
        if 'application/json' in content_type:
            obj = response.json()
            obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
            print(obj_json)
        else:
            print('\t<HTML> / non-JSON content>')


    #----------------- API REPORT (7-in-1) -----------------
    """ ⚠️ USE with .expect_response() only """
    @staticmethod
    def api_report(response):
        API.api_title()
        API.api_url(response)
        API.api_method(response)
        API.api_status_code(response)
        API.api_request_headers(response)
        API.api_response_headers(response)
        API.api_request_body(response)
        API.api_response_body(response)

