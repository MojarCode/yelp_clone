from django.core.mail import EmailMessage
from rest_framework import serializers

from project.restaurant.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "content", "created", "modified", "user", "rating", "restaurant", "comment", "review_likes"]
        # this field cannot be changed. Alternatively, we could update
        # the date if we update the post, then this wouldn't be here
        read_only_fields = ["id", "user", "created", "modified", "restaurant"]

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Update user profile creation",
            body=f"Update user profile creation",
            to=[email],
        )
        message.send()

    def create(self, validated_data):
        review = Review.objects.create(
            # **validated_data,
            content=validated_data.get("content"),
            rating=validated_data.get("rating"),
            restaurant=self.context.get("request").restaurant,
            # alternative way to pass all the fields is to use
            # just **validated_data
            user=self.context.get("request").user,
        )
        self.send_notification_email(
            email=self.context.get('request').user.email
        )
        return review
