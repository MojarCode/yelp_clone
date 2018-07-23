from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SearchDataSerializer(serializers.Serializer):
    SEARCHTYPES = [
        ('restaurant', 'restaurant'),
        ('review', 'review'),
        ('user', 'user'),
    ]

    search_type = serializers.ChoiceField(choices=SEARCHTYPES)
