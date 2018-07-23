from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from project.restaurant.models import Restaurant

User = get_user_model()


class RestaurantRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "user"]
        read_only_fields = fields


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', "name", "country", "street", "city", "zip", "website", "phone_number", "email", "opening_hours",
                  'image', 'status', 'category']
        read_only_fields = ['id']

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Restaurant creation",  # backend is http://aquarius.propulsion-learn.ch/backend/api/
            body=f"Thank you, that you created a new Restaurant",
            to=[email],
            # here we put [] around email so that we could use
            # this for multiple user emails. Otherwise that would not work.
        )
        message.send()

    def create(self, validated_data):

        restaurant = Restaurant.objects.create(
            # **validated_data,
            name=validated_data.get("name"),
            country=validated_data.get("country"),
            street=validated_data.get("street"),
            city=validated_data.get("city"),
            zip=validated_data.get("zip"),
            website=validated_data.get("website"),
            phone_number=validated_data.get("phone_number"),
            opening_hours=validated_data.get("opening_hours"),
            image=validated_data.get("image"),
            status=validated_data.get("status"),
            category=validated_data.get("category"),

            # alternative way to pass all the fields is to use
            # just **validated_data
        )
        self.send_notification_email(
            email=validated_data.get("email")
        )

        return restaurant
