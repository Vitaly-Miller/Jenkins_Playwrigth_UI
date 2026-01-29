"""
Create user
TC_00_000_00
"""
from playwright.sync_api import Page
from faker import Faker
import random
from playwright.sync_api import expect
import requests

#=======================================================================================================================
def test_create_user_non_pom(page: Page):
    # ==================== <Login> page ====================
    # Open <Login> page
    page.goto('http://localhost:8080/login')

    # Page elements locators:
    admin_username_field = page.locator('#j_username')
    admin_password_field = page.locator('#j_password')
    sign_in_btn = page.locator('button[name="Submit"]')

    # Admin credentials:
    admin_username = 'Vitaly_Miller'
    admin_password = 'test_Pass_123'
    api_token = '11baf1d6f2b5f2a3d4eaa977191ae9117e'

    # Fill page fields with admin credentials:
    admin_username_field.fill(admin_username)                 # Enter Admin username
    admin_password_field.fill(admin_password)                 # Enter Admin password

    # Click <Sign in> button
    sign_in_btn.click()                                       # Click -→ <Main> page (Dashboard)                         http://localhost:8080/

    # =============== <Main> page (Dashboard) ==============
    # Page elements locators:
    manage_jenkins_btn = page.get_by_role('link', name='Manage Jenkins')

    # Click <Manage Jenkins btn> ⚙️button
    manage_jenkins_btn.click()                                # Click -→ <Manage Jenkins> page                           http://localhost:8080/manage/

    # ================ <Manage Jenkins> page ===============
    # Page elements locators:
    users_link = page.get_by_text('Users', exact=True)

    # Click <Users> link
    users_link.click()                                        # Click -→ <Jenkins’ own User Database> page (Table)       http://localhost:8080/manage/securityRealm

    # ===== <Jenkins’ own User Database> page (Table) ======
    # Page elements locators:
    plus_create_user_btn = page.get_by_role("link", name="Create User")

    # Click <Create User> button
    plus_create_user_btn.click()                              # Click -→ <Create User> page                              http://localhost:8080/manage/securityRealm/addUser

    # ================== <Create User> page ================
    # Page elements locators:
    username_field = page.locator('input[id="username"]')
    password_field = page.locator('input[name="password1"]')
    confirm_password_field = page.locator('input[name="password2"]')
    full_name_field = page.locator('input[name="fullname"]')
    email_field = page.locator('input[name="email"]')
    create_user_btn = page.locator('button[name="Submit"]')

    # Data Generators:
    fake = Faker()                                            # Fake user data generator
    random_num = random.randint(10, 99)                 # Random numbers generator (10-99)

    # New user credentials (fake data):
    username = f'Username-{random_num}'
    password = fake.password()
    confirm_password = password
    user_full_name = fake.name()
    email = fake.email()

    # Fill page fields:
    username_field.fill(username)                             # Enter username
    password_field.fill(password)                             # Enter password
    confirm_password_field.fill(confirm_password)             # Enter confirm password
    full_name_field.fill(user_full_name)                      # Enter user full name
    email_field.fill(email)                                   # Enter user email

    # Click <Create User> button
    create_user_btn.click()                                   # Click -→ <Jenkins’ own User Database> page (Table)       http://localhost:8080/securityRealm/

    # ===== <Jenkins’ own User Database> page (Table) ======
    # Page elements locators:
    table_user_id = page.locator(f'td > a[href="user/{username.lower()}/"]')
    table_user_name = page.locator(f'//td[normalize-space()="{user_full_name}"]')


    # =================== ✅ EXPECTATIONS: =================
    # The created User ID appeared in the table
    expect(table_user_id, f'❌User ID "{username}" not found!').to_have_text(username)
    # The created User Full name appeared in the table
    expect(table_user_name, f'❌User Full Name "{user_full_name}" not found!').to_have_text(user_full_name)



    # ============== 🧹 CLEANUP (after test): ==============
    # ************** (UI) Delete created User **************
    # Dropdown menu elements locators:
    user_dropdown_menu_chevron = page.locator(f'button[data-href$="user/{username.lower()}/"]')
    dropdown_menu_delete_btn = page.locator(f'button[href="/user/{username.lower()}/doDelete"]')
    delete_yes_bnt = page.locator('button[data-id="ok"]')

    # Click action:
    user_dropdown_menu_chevron.click()                        # Click -→ Open user dropdown menu
    dropdown_menu_delete_btn.click()                          # Click <Delete> button
    delete_yes_bnt.click()                                    # Click <Yes> button (Confirm deletion)

    # ******** (API) Delete created User (optional) ********
    requests.post(
        url=f'http://localhost:8080/user/{username}/doDelete',
        auth=(admin_username, api_token)
    )

#-----------------------------------------------------------------------------------------------------------------------