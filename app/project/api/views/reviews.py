from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from project.api.permissions import IsOwnerOrReadOnly

from project.api.serializers.reviews import ReviewSerializer
from project.restaurant.models import Restaurant, Review, ReviewLike

User = get_user_model()


class RestaurantReviewsView(GenericAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Restaurant.objects.all()

    def get(self, request, **kwrags):
        restaurant = self.get_object()
        # reviews = Review.objects.filter(restaurant=restaurant)
        serializer = ReviewSerializer(restaurant.review.all(), many=True)
        return Response(serializer.data)


class ReviewCreateView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Restaurant.objects.all()

    def post(self, request, **kwargs):
        restaurant = self.get_object()
        request.restaurant = restaurant
        serializer = ReviewSerializer(data=request.data,
                                      context={
                                          "request": request,
                                      }, )  # passing request to the context of serializer
        serializer.is_valid(raise_exception=True)
        review = serializer.create(serializer.validated_data)
        return Response(ReviewSerializer(review).data)


class ReviewByUserView(GenericAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = ReviewSerializer(user.reviews.all(), many=True)
        return Response(serializer.data)


class GetPostDeleteReviewView(GenericAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get(self, request, review_id):
        review = Review.objects.get(id=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def post(self, request, review_id):
        review = Review.objects.get(id=review_id)
        self.check_object_permissions(request, review)
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, review_id):
        review = Review.objects.get(id=review_id)
        self.check_object_permissions(request, review)
        review.delete()
        return Response("OK")


class ReviewLikeDislikeView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly
    ]

    @staticmethod
    def send_notification_email(email):
        message = EmailMessage(
            subject="Update user profile creation",
            body=f"Update user profile creation",
            to=[email],
        )
        message.send()

    def post(self, request, review_id):
        likes = ReviewLike.objects.filter(review_id=review_id, user_id=request.user.id).count()
        if likes > 0:
            return Response("You already liked this post")
        else:
            ReviewLike.objects.create(review_id=review_id, user_id=request.user.id)
            self.send_notification_email(
                email=request.user.email
            )
            return Response("Added a like")

    def delete(self, request, review_id):
        likes = ReviewLike.objects.filter(review_id=review_id, user_id=request.user.id).count()
        if likes > 0:
            ReviewLike.objects.get(review_id=review_id, user_id=request.user.id).delete()
            return Response("Like deleted.")
        else:
            return Response("You did not like this post before or already deleted your like.")


class LikedReviewsView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        reviews = Review.objects.filter(review_likes__user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class CommentedReviewsView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        reviews = Review.objects.filter(comment__user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
