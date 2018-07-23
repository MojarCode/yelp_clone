from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from project.api.tests.master_tests import MasterTestWrapper

User = get_user_model()


class RegistrationViewTest(APITestCase):
    endpoint = "api:registration"
    methods = ["POST"]

    def get_url(self, *args, **kwargs):
        return reverse(self.endpoint, args=args, kwargs=kwargs)

    def get_kwargs(self):
        return self.kwargs

    def setUp(self):
        super().setUp()
        self.new_user = User.objects.create_user(
            username="some_email@gmail.com",
            email="some_email@gmail.com",
            is_active=False,
        )

    def test_registration(self):
        url = self.get_url()
        response = self.client.post(url, data={"email": "new_user@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        num_users = User.objects.count()
        self.assertEquals(num_users, 2)
        num_results = User.objects.filter(username="new_user@gmail.com").count()
        self.assertEquals(num_results, 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Luna registration')
        new_user = User.objects.get(username="new_user@gmail.com")
        self.assertEqual(mail.outbox[0].body[-30:-25], new_user.user_profile.registration_code)

    def test_registration_existing_user(self):
        url = self.get_url()
        response = self.client.post(url, data={"email": "some_email@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["email"][0], "User with this email address already exists.")


class RegistrationValidationViewTest(MasterTestWrapper.MasterTests):
    endpoint = "api:registration-validation"
    methods = ["POST"]

    def test_unauthorized_request(self):
        pass

    def setUp(self):
        super().setUp()
        self.new_user = User.objects.create_user(
            username="new_user@gmail.com",
            is_active=False,
        )

    def test_registration_validation(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": self.new_user.user_profile.registration_code,
            "password": "password",
            "password_repeat": "password",
            "first_name": "new",
            "last_name": "user"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_user = User.objects.get(username="new_user@gmail.com")
        self.assertEqual(new_user.first_name, "new")
        self.assertEqual(new_user.last_name, "user")
        self.assertEqual(new_user.is_active, True)

    def test_wrong_validation_code(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": "12423",
            "password": "password",
            "password_repeat": "password",
            "first_name": "new",
            "last_name": "user"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["code"][0], "Wrong validation code or already validated!")

    def test_passwords_not_matching(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": self.new_user.user_profile.registration_code,
            "password": "password",
            "password_repeat": "12345",
            "first_name": "new",
            "last_name": "user"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"][0], "Passwords are not equal!")
