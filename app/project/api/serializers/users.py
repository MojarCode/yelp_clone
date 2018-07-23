from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model
# from django.core.mail import EmailMessage
from rest_framework import serializers

# from project.restaurant.models import Restaurant, Review, Comment
from project.user.models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'location', 'things_i_love', 'description', 'joined_date', 'profile_image', 'phone_number']
        read_only_fields = ['id', 'joined_date']


class Reviews(object):
    pass


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'user_profile']
        read_only_fields = ['id', 'email']


class UserUpdateProfileSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='username',
        write_only=True,
        required=False,
        allow_blank=True,

    )
    location = serializers.CharField(
        label='location',
        write_only=True,
        required=False,
        allow_blank=True

    )
    phone_number = serializers.CharField(
        label='phone_number',
        write_only=True,
        required=False,
        allow_blank=True

    )
    things_i_love = serializers.CharField(
        label='Things I Love',
        write_only=True,
        required=False,
    )
    profile_image = serializers.CharField(
        label='Project Image',
        write_only=True,
        required=False,
        allow_blank=True
    )
    joined_date = serializers.DateTimeField(
        label='Joined Date',
        write_only=True,
        required=False,

    )
    description = serializers.CharField(
        label='Description',
        write_only=True,
        required=False,
        allow_blank=True

    )

    def validate_email(self, email):
        try:
            return User.objects.get(
                email=email,
                is_active=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'You have registered with different email!'
            )

    def validate_location(self, location):

        if location == "":
            raise serializers.ValidationError({
                'location': 'Please enter location!'
            })
        else:
            return location

    def validate_username(self, username):

        if username == "":
            raise serializers.ValidationError({
                'username': 'Please enter Username!'
            })
        else:
            return username

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Update user profile creation",
            body=f"Update user profile creation",
            to=[email],
        )
        message.send()

    def save(self, validated_data):
        user = self.context.get('request').user
        profile = Profile.objects.get(user=user)
        user.username = validated_data.get('username')
        profile.location = validated_data.get('location')
        profile.phone_number = validated_data.get('phone_number')
        profile.things_i_love = validated_data.get('things_i_love')
        profile.description = validated_data.get('description')
        profile.joined_date = validated_data.get('joined_date')
        profile.profile_image = validated_data.get('profile_image')
        profile.save()
        user.save()

        self.send_notification_email(
            email=self.context.get('request').user.email
        )

        return user
