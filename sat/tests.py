from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import json
class TestLoginLogout(APITestCase):
    def setUp(self) -> None:
        self.creds = dict(username="tomsa", password="123456abcd...",email="tomsaso@gmail.com")
        User.objects.create_user(**self.creds)
        return super().setUp()
    def test_user_login_logut(self):
        response = self.client.post("/login/", data=self.creds, format="json")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/companies/")
        self.assertEqual(response.status_code,200)
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/companies/")
        self.assertEqual(response.status_code, 403)

class TestComapnies(APITestCase):
    def setUp(self) -> None:
        self.creds = dict(username="tomsa", password="123456abcd...",email="tomsaso@gmail.com")
        self.user = User.objects.create_user(**self.creds)
        self.creds2 = dict(username="tomsa2", password="123456abcd...",email="tomsaso@gmail.com")
        self.user2 = User.objects.create_user(**self.creds2)
        self.client.login(**self.creds)
        self.company =  {
            "company_name":"Test1",
            "description": "Test1 desc",
            "number_of_employees":5
        }
        return super().setUp()
    def test_companies_create(self):
        company = self.company
        response = self.client.post("/companies/", data=company, format="json")
        self.assertEqual(response.status_code, 201)
        company['id'] = 1
        self.assertEqual(response.json(), company)

    def test_companies_limit_5(self):
        company = self.company
        for i in range(5):
            response = self.client.post("/companies/", data=company,format="json")
            self.assertEqual(response.status_code, 201)
        response = self.client.post("/companies/", data=company,format="json")
        self.assertEqual(response.status_code, 400)
    def test_company_get_by_id(self):
        response = self.client.post("/companies/", data=self.company,format="json")
        self.assertEqual(response.status_code, 201)
        company = response.json()
        response = self.client.get(f"/companies/{company['id']}")
        company['owner'] = self.user.id
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), company)

    def test_company_object_permissons(self):
        response = self.client.post("/companies/", data=self.company,format="json")
        company_id = response.json()['id']
        self.client.logout()
        self.client.login(**self.creds2)
        response = self.client.get(f"/companies/{company_id}")
        self.assertEqual(response.status_code, 403)

    def test_company_display_fields(self):
        response = self.client.post("/companies/", data=self.company,format="json")
        response = self.client.get("/companies/")
        data = response.json()
        company = data['results'][0]
        fields = ['id', "company_name", "description", "number_of_employees"]
        self.assertEqual(list(company.keys()), fields)

    def test_company_unable_to_delete(self):
        response = self.client.post("/companies/", data=self.company,format="json")
        company_id = response.json()['id']
        response = self.client.delete(f"/companies/{company_id}")
        self.assertEqual(response.status_code, 405)

    def test_update_only_employees_field(self):
        response = self.client.post("/companies/", data=self.company,format="json")
        company_id = response.json()['id']
        company2 = {
            "company_name":"Test2",
            "description": "Test2 desc",
            "number_of_employees":50
        }
        response = self.client.patch(f"/companies/{company_id}", data=company2)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/companies/{company_id}")
        data = response.json()
        self.assertNotEqual(data['company_name'], company2["company_name"])
        self.assertNotEqual(data['description'], company2["description"])
        self.assertEqual(data['number_of_employees'], company2["number_of_employees"])