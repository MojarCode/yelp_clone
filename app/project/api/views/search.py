from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.serializers.search import SearchDataSerializer
from project.api.serializers.users import UserSerializer
from project.restaurant.models import Review, Restaurant

User = get_user_model()


# @route   GET api/search
# @desc    Get the review, restaurant or user profile
# @access  Public
class SearchListView(APIView):
    serializer_class = SearchDataSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        search_type = serializer.validated_data.get("search_type")
        search_string = self.request.query_params.get('search')
        if search_type == "user":
            users = User.objects.all()
            queryset = users.filter(
                Q(username__contains=search_string) |
                Q(first_name__contains=search_string) |
                Q(last_name__contains=search_string)
            )
            return Response(UserSerializer(queryset, many=True).data)
        elif search_type == "review":
            reviews = Review.objects.all()
            queryset = reviews.filter(
                Q(content__contains=search_string) |
                Q(comment__contains=search_string)
            )
            return Response(UserSerializer(queryset, many=True).data)
        elif search_type == "restaurant":
            restaurants = Restaurant.objects.all()
            queryset = restaurants.filter(
                Q(name__contains=search_string) |
                Q(street__contains=search_string) |
                Q(country__contains=search_string) |
                Q(category__contains=search_string)
            )
            return Response(UserSerializer(queryset, many=True).data)
