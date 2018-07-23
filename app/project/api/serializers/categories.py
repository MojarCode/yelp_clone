from rest_framework import serializers

from project.restaurant.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        # this field cannot be changed. Alternatively, we could update
        # the date if we update the post, then this wouldn't be here
        read_only_fields = ["id", "name"]
