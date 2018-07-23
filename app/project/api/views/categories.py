from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from project.api.serializers.categories import CategorySerializer
from project.restaurant.models import Category


class GetCategoriesView(GenericAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
