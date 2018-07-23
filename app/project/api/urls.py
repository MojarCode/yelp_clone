from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from project.api.views.comments import CreateCommentOnReviewView, DeleteCommentOnReviewView, \
    LikeRemoveLikeCommentOnReviewView, GetCommentsForReviewView
from project.api.views.categories import GetCategoriesView
from project.api.views.registration import RegistrationView, RegistrationValidationView
from project.api.views.restaurants import PostNewRestaurantView, GetAllRestaurantsView, GetRestaurantByNameView, \
    GetRestaurantByCategoryView, GetRestaurantByUserView, GetUpdateDeleteRestaurantByIDView
from project.api.views.search import SearchListView
from project.api.views.users import GetUpdateUserProfileView, GetAllUsersView, GetSpecificUserProfileView, GetUserView
from project.api.views.password_reset import PasswordResetView, PasswordResetValidationView
from project.api.views.reviews import RestaurantReviewsView, ReviewCreateView, ReviewByUserView, \
    GetPostDeleteReviewView, ReviewLikeDislikeView, LikedReviewsView, CommentedReviewsView

app_name = "api"

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("registration/validation/", RegistrationValidationView.as_view(), name="registration-validation"),
    path("me/", GetUpdateUserProfileView.as_view(), name="show-update-userprofile"),
    path("users/", GetUserView.as_view(), name="search-for-a-user"),
    path("users/list/", GetAllUsersView.as_view(), name="list-all-users"),
    path("users/<int:user_id>/", GetSpecificUserProfileView.as_view(), name="get-user-profile"),
    path("review/comment/new/<int:pk>/", CreateCommentOnReviewView.as_view(), name="comment-on-review"),
    path("review/comment/<int:pk>/", DeleteCommentOnReviewView.as_view(), name="delete-comment-on-review"),
    path("review/comment/like/<int:pk>/", LikeRemoveLikeCommentOnReviewView.as_view(), name="like-comment"),
    path("review/comment/like/<int:pk>/", LikeRemoveLikeCommentOnReviewView.as_view(), name="delete-comment-on-review"),
    path("review/comments/<int:review_id>/", GetCommentsForReviewView.as_view(), name='get-comment-for-review'),
    path("auth/password-reset/", PasswordResetView.as_view(), name="password-reset"),
    path("auth/password-reset/validate/", PasswordResetValidationView.as_view(), name="password-reset-validation"),
    path("reviews/restaurant/<int:pk>/", RestaurantReviewsView.as_view(), name="restaurant-reviews"),
    path("reviews/new_review/<int:pk>/", ReviewCreateView.as_view(), name="create-review"),
    path("reviews/user/<int:user_id>/", ReviewByUserView.as_view(), name="show-reviews-for-user"),
    path("reviews/<int:review_id>/", GetPostDeleteReviewView.as_view(), name="get-post-delete-review"),
    path("reviews/like/<int:review_id>/", ReviewLikeDislikeView.as_view(), name="like-dislike-review"),
    path("reviews/likes/", LikedReviewsView.as_view(), name="liked-reviews"),
    path("reviews/comments/", CommentedReviewsView.as_view(), name="commented-reviews"),
    path("category/list/", GetCategoriesView.as_view(), name='get-list-of-categories'),
    path("restaurants/new/", PostNewRestaurantView.as_view(), name="create-new-restaurant"),
    path("restaurants/", GetAllRestaurantsView.as_view(), name="get-list-of-restaurants"),
    path("restaurants/?search=<str:search_string>/", GetRestaurantByNameView.as_view(), name="get-restaurant-by-name"),
    path("restaurants/category/<int:category_id>/", GetRestaurantByCategoryView.as_view(), name="get-restaurant-by-category"),
    path("restaurants/user/<int:user_id>/", GetRestaurantByUserView.as_view(), name="get-restaurant-by-userview"),
    path("restaurants/<int:restaurant_id>/", GetUpdateDeleteRestaurantByIDView.as_view(), name="get-update-delete-restaurant"),

    path("search/", SearchListView.as_view(), name="search-user-review-restaurant"),
]
