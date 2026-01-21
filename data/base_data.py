"""
BASE data
"""
from dotenv import load_dotenv
import os

#======================================================= UI DATA =======================================================
# Reading .env
load_dotenv()

class Base:
    # Base URL
    URL = os.getenv('BASE_URL')            # Base URL

    # Admin data (Credentials)
    USERNAME = os.getenv('USERNAME')       # Username (Admin)
    PASSWORD = os.getenv('PASSWORD')       # Password (Admin)
    API_TOKEN = os.getenv('API_TOKEN')     # Сгенерирован в admin-аккаунте Jenkins



#===================================================== ↕ API DATA ======================================================
    #----------------- Endpoints ---------------
    # Users endpoints
    CREATE_USER_ENDPOINT = f'/securityRealm/createAccountByAdmin'
    DELETE_USER_ENDPOINT = lambda username: f'/user/{username}/doDelete'

    # Items endpoints
    CREATE_ITEM_ENDPOINT = f'/view/all/createItem'
    DELETE_ITEM_ENDPOINT = lambda item_name: f'/job/{item_name}/doDelete'


    # ----- Create Modes params (mode='') ------
    PIPELINE_API_MODE = 'org.jenkinsci.plugins.workflow.job.WorkflowJob'
    FREE_STYLE_PROJECT_API_MODE = 'hudson.model.FreeStyleProject'
    MULTI_CONFIGURATION_PROJECT_API_MODE = 'hudson.matrix.MatrixProject'
    FOLDER_API_MODE = 'com.cloudbees.hudson.plugins.folder.Folder'

    # -------------- Error messages --------------
    # Invalid Item type error
    MODE_ERROR = lambda item_type: f"""
        ❌Invalid Item type: {item_type}
        Expected: -> "pipeline"
                  -> "free_style_project"
                  -> "multi_configuration_project"
                  -> "folder"
        """