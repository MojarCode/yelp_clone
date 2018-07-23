from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from project.user.models import Profile

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="E-Mail address"
    )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError(
                "User with this email address already exists."
            )
        except User.DoesNotExist:
            return value

    @staticmethod
    def send_registration_email(email, code):
        message = EmailMessage(
            subject="Luna registration",  # backend is http://aquarius.propulsion-learn.ch/backend/api/
            body=f"This is your registration link =>> http://aquarius.propulsion-learn.ch/registration/validation?code={code}&email={email}",
            # body=f"This is your registration link =>> http://localhost:3000/registration/validation?code={code}&email={email}",
            to=[email],
            # here we put [] around email so that we could use
            # this for multiple user emails. Otherwise that would not work.
        )
        message.send()

    def register_user(self, email):
        new_user = User.objects.create_user(
            username=email,
            email=email,
            is_active=False
        )
        self.send_registration_email(
            email=email,
            code=new_user.user_profile.registration_code,
        )
        return new_user


class RegistrationValidationSerializer(serializers.Serializer):
    code = serializers.CharField(
        label='Validation code',
        write_only=True,
    )
    password = serializers.CharField(
        label='password',
        write_only=True,
    )
    password_repeat = serializers.CharField(
        label='password',
        write_only=True,
    )
    username = serializers.CharField(
        label='Username'
    )
    location = serializers.CharField(
        label='Location'
    )
    email = serializers.EmailField(
        label='Email'
    )

    def validate_email(self, value):
        try:
            return User.objects.get(
                email=value,
                is_active=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'You have registered with different email!'
            )

    def validate(self, data):
        user = data.get('email')
        if user.user_profile.registration_code != data.get('code'):
            raise serializers.ValidationError({
                'code': 'Wrong code entered!'
            })
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password': 'Passwords are not equal!'
            })
        return data

    def save(self, validated_data):
        user = validated_data.get('email')
        profile = Profile.objects.get(user=user)
        user.username = validated_data.get('username')
        profile.location = validated_data.get('location')
        user.is_active = True
        user.set_password(validated_data.get('password'))
        user.save()
        profile.save()
        return user
