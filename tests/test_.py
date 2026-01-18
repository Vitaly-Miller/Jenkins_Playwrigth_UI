from data.generators import Fake
from func.api import API

#=======================================================================================================================
def test_api_create_items():
    API.create_pipeline()
    API.create_free_style_project()
    API.create_multi_configuration_project()
    API.create_folder()

    #API.delete_all_jobs()
#-----------------------------------------------------------------------------------------------------------------------
def test_api_create_user():
    API.create_user()