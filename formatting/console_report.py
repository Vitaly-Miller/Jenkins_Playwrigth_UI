"""
✨Console report (beautify)
"""
import json
from formatting.colors import *

#=======================================================================================================================
class APIreport:
    """ ⚠️USE with .expect_response() only """
    # ------------------------- Base ----------------------
    # Title
    @staticmethod
    def title():
        print(f'\n\n{B_CYAN}🅰🅿︎🅸 🆁🅴🅿︎🅾🆁🆃{RESET}')

    # URL
    @staticmethod
    def url(response):
        obj = response.request.url
        print(f'\n{GRAY}┌╴Request URL: {obj}{RESET}')

    # Method
    @staticmethod
    def method(response):
        obj = response.request.method
        if obj == 'GET':       color = B_GREEN
        elif obj == 'POST':    color = BEIGE
        elif obj == 'PUT':     color = B_BLUE
        elif obj == 'PATCH':   color = B_PURPLE
        elif obj == 'DELETE':  color = B_RED
        elif obj == 'OPTIONS': color = PINK
        else: color = RESET
        print(f'{GRAY}├╴HTTP Method: {color}{obj}{RESET}')

    # Status code
    @staticmethod
    def status_code(response):
        obj = response.status
        if obj < 200:   color = SUNRISE              # 1xx
        elif obj < 300: color = BRIGHT_GREEN         # 2xx
        elif obj < 400: color = SUNRISE              # 3xx
        elif obj < 500: color = RED                  # 4xx
        elif obj < 600: color = ORANGE               # 5xx
        else: color = RESET
        print(f'{GRAY}└╴Status code: {color}{obj}{RESET}')

    # ------------------------ JSON -----------------------
    # Request headers ⮕
    @staticmethod
    def request_headers(response):
        print(f'\n{BROWN}REQUEST HEADERS{GRAY}: ⮕')
        obj = dict(response.request.headers)
        obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
        print(f'{obj_json}{RESET}')

    # Request body ⮕
    @staticmethod
    def request_body(response):
        print(f'\n{GREEN}REQUEST BODY{GRAY}: ⮕')
        if response.request.post_data:  # 👈 <.post_data> for <page.expect_response()>
            obj = json.loads(response.request.post_data)
            obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
            print(f'{obj_json}{RESET}')
        else:
            print(f'{{\n\t<None>\n}}{RESET}')

    # Response headers ⬅︎
    @staticmethod
    def response_headers(response):
        print(f'\n{BROWN_ORANGE}RESPONSE HEADERS{GRAY}: ⬅︎')
        obj = dict(response.headers)
        obj_json = json.dumps(obj, indent=4,ensure_ascii=False)
        print(f'{obj_json}{RESET}')

    # Response body ⬅︎
    @staticmethod
    def response_body(response):
        print(f'\n{BLUE}RESPONSE BODY{GRAY}: ⬅︎')
        content_type = response.headers.get('content-type', '')
        if 'application/json' in content_type:
            obj = response.json()
            obj_json = json.dumps(obj, indent=4, ensure_ascii=False)
            print(f'{obj_json}{RESET}')
        else:
            print(f'\t<HTML> / non-JSON content>')
    # ---------------------------------------------------