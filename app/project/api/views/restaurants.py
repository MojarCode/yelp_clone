from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from project.api.permissions import IsOwnerOrReadOnly
from project.api.serializers.restaurants import RestaurantRatingSerializer, RestaurantSerializer
from project.api.serializers.users import UserSerializer
from project.restaurant.models import Restaurant


class PostNewRestaurantView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, **kwargs):
        serializer = RestaurantSerializer(data=request.data,
                                          context={
                                              "request": request
                                          }, )  # passing request to the context of serializer
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.create(serializer.validated_data)
        return Response(RestaurantSerializer(restaurant).data)


# @route   GET api/restaurants/
# @desc    Get the list of all the restaurants
# @access  Public
class GetAllRestaurantsView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        return Response(RestaurantRatingSerializer(Restaurant.objects.all(), many=True).data)


# @route   GET api/restaurants/?search=<str:search_string/>
# @desc    Get the restaurant by name
# @access  Public
class GetRestaurantByNameView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, restaurant_id):
        return Response(RestaurantRatingSerializer(Restaurant.objects.filter(restaurant_id)).data)


# @route   GET api/restaurants/<int:category_id/>
# @desc    Get restaurants by category
# @access  Public
class GetRestaurantByCategoryView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, category_id):
        return Response(UserSerializer(User.objects.filter(category_id)).data)


# @route   GET api/restaurants/<int:user_id/>
# @desc    Get restaurants created by specific user
# @access  Public
class GetRestaurantByUserView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)


# @route   GET/POST api/restaurants/<int:id/>
# @desc    Get, update and delete a restaurant by ID
# @access  Public
class GetUpdateDeleteRestaurantByIDView(GenericAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Update user profile creation",
            body=f"Update user profile creation",
            to=[email],
        )
        message.send()

    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        self.check_object_permissions(request, restaurant)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.send_notification_email(
            email=request.user.email
        )

        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        self.check_object_permissions(request, restaurant)
        restaurant.delete()
        return Response("OK")
