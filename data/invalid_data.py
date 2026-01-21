"""
❌Invalid data
(for negative testing)
"""
from data.base_data import Base

#=======================================================================================================================
class Invalid:
    #----------------------- Base URL ---------------------
    URL_EMPTY = ''                                                # Empty
    URL_SPACE = ' '                                               # Space only
    URL = 'http://incorrect_url'

    #-------------- Admin data (Credentials) --------------
    # Username
    USERNAME = 'WrongUsername'                                    # Invalid username
    USERNAME = ''                                                 # <>
    USERNAME_SPACE = ' '                                          # < >
    USERNAME_SPACE_END = Base.USERNAME + ' '                      # <Username >
    USERNAME_SPACE_BEGIN = ' ' + Base.USERNAME                    # < Username>

    #----------------------- Password ---------------------
    PASSWORD = 'Wrong_Password_135'                               # Invalid Password
    PASSWORD_EMPTY = ''                                           # <>
    PASSWORD_SPACE = ' '                                          # < >
    PASSWORD_123 = '123'                                          # <123>

    #------------------- Confirm password -----------------
    CONFIRM_PASSWORD = 'Wrong_confirm_password_135'               # Invalid confirm password
    CONFIRM_PASSWORD_EMPTY = ''                                   # <>
    CONFIRM_PASSWORD_SPACE = ' '                                  # < >
    CONFIRM_PASSWORD_SPACE_END = Base.PASSWORD + ' '              # <Valid_Password  >
    CONFIRM_PASSWORD_SPACE_BEGIN = ' ' + Base.PASSWORD            # <  Valid_Password>
    CONFIRM_PASSWORD_SPACES = ' ' + Base.PASSWORD + ' '           # <  Valid_Password  >


    #----------------------- API token --------------------
    TOKEN_WRONG = '11aaa1a1a1a1a1a1a1aaa111111aa1111a'            # Invalid token
    TOKEN_EMPTY = ''                                              # <>
    TOKEN_SPACE = ' '                                             # < >
    TOKEN_SPACE_END = Base.API_TOKEN + ' '                        # <Valid_API_token  >
    TOKEN_SPACE_BEGIN = ' ' + Base.API_TOKEN                      # <  Valid_API_token>
    TOKEN_SPACES = ' ' + Base.API_TOKEN + ' '                     # <  Valid_API_token  >

    #----------------------- Email ------------------------
    EMAIL_EMPTY = ''                                              # <>
    EMAIL_NO_AT_SIGN = 'no_at_sign_email.com'                     # <no_at_sign_email.com>
    EMAIL_NO_DOT = 'no_dot_emailcom'                              # <no_dot_emailcom>
    EMAIL_NO_DOMAIN = 'no_domain_in@email'                        # <no_domain_in@email>
    EMAIL_SPACE_END = 'spece_end@email.com  '                     # <spece_end@email.com >
    EMAIL_SPACE_BEGIN = ' spece_begin@email.com'                  # < spece_begin@email.com>
    EMAIL_SPACES = ' space in@email.com  '                        # < speces@email.com  >
    EMAIL_SPACE_IN = 'space in@email.com'                         # <space in@email.com>


    # Items
    ITEM_NAME_EMPTY = ''                                          # Empty
    ITEM_NAME = 'Invalid_item_name_#'                             # Non accessible symbol <#>