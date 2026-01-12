"""
Data generators
(Fake & Random data)
"""
import random
from faker import Faker

#=======================================================================================================================
# Setup:
fake = Faker()
random_10_99 = random.randint(10, 99)                              # 10 ≤ int ≤ 99


class Fake:
    #---------- User data (credentials): ----------
    username = f'Username-{random_10_99}'                                # Username-58
    user_password = fake.password()                                      #
    user_full_name = fake.name()                                         # John Connor (Last name + First name)
    user_email = fake.email()                                            # john.connor@example.com

    #---------------- Items names: ----------------
    pipeline_name = f'Pipline-{random_10_99}'                            # Pipline-82
    folder_name = f'Folder-{random_10_99}'                               # Folder-31
    freestyle_project_name = f'Freestyle Project-{random_10_99}'         # Freestyle Project-74

    view_name = f'View-{random_10_99}'                                   # View-45
