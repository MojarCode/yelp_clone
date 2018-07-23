from django.contrib import admin
from project.restaurant.models import Review, Restaurant, ReviewLike, Comment, CommentLike, Category

admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(ReviewLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Category)
