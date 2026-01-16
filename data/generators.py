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


class Fake:
    #---------- User data (credentials): ----------
    username = f'Username-{random_10_99}'                                             # Username-58
    user_password = fake.password()                                                   #
    user_full_name = fake.name()                                                      # John Connor (Last + First name)
    user_email = fake.email()                                                         # john.connor@example.com

    #---------------- Items names: ----------------
    # Item Types
    pipeline_name = f'Pipline-{random_10_99}'                                         # Pipline-82
    folder_name = f'Folder-{random_10_99}'                                            # Folder-31
    freestyle_project_name = f'Freestyle Project-{random_10_99}'                      # Freestyle Project-74
    multi_configuration_project_name = f'Multi-configuration Project-{random_10_99}'  # Multi-configuration Project-21

    # User-friendly names
    display_item_name = f'Display name-{random_10_99}'                                # Display Name-58
    view_item_name = f'View name-{random_10_99}'                                      # View-45