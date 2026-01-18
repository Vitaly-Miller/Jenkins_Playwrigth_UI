"""
API helpers
"""
from data.base_data import Base
import requests
from formatting.console_report import APIreport

#=======================================================================================================================
class API:
    #------------------------ Users ----------------------
    # Delete user
    @staticmethod
    def delete_user(username: str):
        requests.post(
            url=f"{Base.URL}/user/{username}/doDelete",
            auth=(Base.USERNAME, Base.API_TOKEN))


    #-------------------- Jobs (Items) -------------------
    # Delete job (Item) by nane
    @staticmethod
    def delete_job(job_name: str):
        requests.post(
            url=f"{Base.URL}/job/{job_name}/doDelete",
            auth=(Base.USERNAME, Base.API_TOKEN))


    # Delete ALL jobs (Items)
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
            api_report: bool = False                                             # NO API report by default
    ):
        with page.expect_response(lambda r: r.status == code) as response_info:  # Перехватить Response с определенным <status code>
            action()                                                             # 👈 Перехватываемый action
            response = response_info.value                                       # Внутренний объект-контейнер => в рабочий Response
            if api_report:
                API.report(response)                                             # API REPORT в консоль if True (optional)
        return response

    # by URL
    @staticmethod
    def api_by_url(
            page,
            action,
            url: str,
            api_report: bool = False                               # NO API report by default
    ):
        with page.expect_response(url) as response_info:           # Перехватить Response c URL
            action()                                               # 👈 Перехватываемый action
            response = response_info.value                         # Внутренний объект-контейнер => в рабочий Response
            if api_report:
                API.report(response)                               # API REPORT в консоль if True (optional)
        return response





    #========== API REPORT (8-in-1) ===========
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