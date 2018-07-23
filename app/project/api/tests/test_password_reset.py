from django.contrib.auth import get_user_model
from django.core import mail
from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper

User = get_user_model()


class PasswordResetView(MasterTestWrapper.MasterTests):
    endpoint = "api:password-reset"
    methods = ["POST"]

    def test_unauthorized_request(self):
        pass

    def setUp(self):
        super().setUp()
        self.new_user = User.objects.create_user(
            username="new_user@gmail.com",
            email="new_user@gmail.com",
            is_active=True,
        )
        self.new_user.user_profile.registration_code = "12345"

    def test_reset_password(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={"email": "new_user@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset request')
        self.new_user = User.objects.get(username="new_user@gmail.com")
        self.assertEqual(mail.outbox[0].body[-30:-25], self.new_user.user_profile.registration_code)

    def test_not_existing_user_pw_reset(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={"email": "some_email@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["email"][0], "User with this email address does not exist.")


class PasswordResetValidationViewTest(MasterTestWrapper.MasterTests):
    endpoint = "api:password-reset-validation"
    methods = ["POST"]

    def test_unauthorized_request(self):
        pass

    def setUp(self):
        super().setUp()
        self.new_user = User.objects.create_user(
            username="new_user@gmail.com",
            email="new_user@gmail.com",
            is_active=True,
        )

    def test_reset_pw_validation(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": self.new_user.user_profile.registration_code,
            "password": "password",
            "password_repeat": "password",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_pw_validation_wrong_code(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": "12345",
            "password": "password",
            "password_repeat": "password",
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["code"][0], "Wrong validation code!")

    def test_reset_pw_not_matching(self):
        url = self.get_url(**self.get_kwargs())
        response = self.client.post(url, data={
            "code": self.new_user.user_profile.registration_code,
            "password": "password",
            "password_repeat": "pasword",
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"][0], "Passwords are not equal!")
