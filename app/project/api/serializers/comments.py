from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers
from project.restaurant.models import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created', 'modified', 'review', 'user']
        read_only_fields = ['id', 'modified', 'created', 'review', 'user']

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Thanks for the Review",
            body=f"Thanks for the Review",
            to=[email],
        )
        message.send()

    def create(self, validated_data):

        comment = Comment.objects.create(
            **validated_data,
            review=self.context.get('request').review,
            user=self.context.get('request').user,
        )

        self.send_notification_email(
            email=self.context.get('request').review.user.email
        )

        return comment
