from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

User = get_user_model()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="E-Mail address"
    )

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            return user.email
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this email address does not exist."
            )

    @staticmethod
    def send_password_reset_email(email, code):
        message = EmailMessage(
            subject="Password reset request",
            body=f"This is your registration link =>> http://aquarius.propulsion-learn.ch/registration/validation?code={code}&email={email}",
            to=[email],
        )
        message.send()

    def update_user(self, email):
        user = User.objects.get(
            email=email
        )
        user.user_profile.generate_new_code()
        self.send_password_reset_email(
            email=email,
            code=user.user_profile.registration_code,
        )
        return user


class PasswordResetValidationSerializer(serializers.Serializer):
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

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password': 'Passwords are not equal!'
            })
        return data

    def validate_code(self, value):
        try:
            return User.objects.get(
                user_profile__registration_code=value,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Wrong validation code!'
            )

    def save(self, validated_data):
        user = validated_data.get('code')
        user.set_password(validated_data.get('password'))
        user.save()
        return user
