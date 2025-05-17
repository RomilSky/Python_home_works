import pytest


class TestProjectsAPI:
    # Позитивные тесты
    def test_create_project_positive(self, projects_api):
        project_data = {
            "title": "Новый тестовый проект",
            "users": {"871a83bf-0e27-427f-8fa8-4e05199470bc": "admin"}
        }
        response = projects_api.create_project(project_data)

        assert response.status_code == 201
        assert "id" in response.json()

    def test_get_project_positive(self, projects_api, existing_project_id):
        response = projects_api.get_project(existing_project_id)

        assert response.status_code == 200
        assert response.json()["id"] == existing_project_id
        assert "title" in response.json()

    def test_update_project_positive(self, projects_api, existing_project_id):
        update_data = {
            "title": "Обновленный ГазПром",
            "users": {"871a83bf-0e27-427f-8fa8-4e05199470bc": "admin"}
        }
        response = projects_api.update_project(existing_project_id, update_data)

        assert response.status_code == 200

        # Негативные тесты
    def test_create_project_negative_missing_title(self, projects_api):
        project_data = {
            "users": {"871a83bf-0e27-427f-8fa8-4e05199470bc": "admin"}
        }
        response = projects_api.create_project(project_data)

        assert response.status_code == 400
        assert "error" in response.json()

    def test_get_project_negative_invalid_id(self, projects_api):
        invalid_id = "invalid-id-123"
        response = projects_api.get_project(invalid_id)

        assert response.status_code == 404
        assert "error" in response.json()

    def test_update_project_negative_invalid_data(self, projects_api, existing_project_id):
        update_data = {
            "invalid_field": "invalid_value"  # Неправильное поле
        }
        response = projects_api.update_project(existing_project_id, update_data)

        assert response.status_code == 400
        assert "error" in response.json()
