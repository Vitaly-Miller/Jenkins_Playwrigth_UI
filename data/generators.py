"""
Data generators
(Fake & Random data)
"""
import random
from faker import Faker

#=======================================================================================================================
# Setup:
fake = Faker()
random_10_99 = random.randint(10, 99)                                           # 10 ≤ int ≤ 99
random_type = random.choice(
    ['pipeline',
     'free_style_project',
     'multi_configuration_project',
     'folder'
     ])

class Fake:
    #---------- User data (credentials): ----------
    username = f'Username-{random_10_99}'                                             # Username-58
    user_password = fake.password()                                                   #
    user_full_name = fake.name()                                                      # John Connor (Last + First name)
    user_email = fake.email()                                                         # john.connor@example.com

    #------------------ Items: --------------------

    item_name = f'Item-{random_10_99}'                                # Default_Item-43
    random_item_type = random_type


    # User-friendly names
    display_item_name = f'Display_name-{random_10_99}'                                # Display Name-58
    view_item_name = f'View_name-{random_10_99}'                                      # View-45