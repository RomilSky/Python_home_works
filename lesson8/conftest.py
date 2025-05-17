import pytest
from lesson8.api.projects import ProjectsAPI

@pytest.fixture
def projects_api():
    base_url = "https://yougile.com/api-v2"
    auth_token = "токен вставить сюда" # вставить действующий токен
    return ProjectsAPI(base_url, auth_token)

@pytest.fixture
def existing_project_id():
    return "c224a008-8cc0-40d8-9309-092664c00905"
