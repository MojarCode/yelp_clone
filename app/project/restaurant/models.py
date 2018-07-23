from django.db import models

from django.conf import settings

from django_countries.fields import CountryField
from django.core.validators import RegexValidator, MaxValueValidator

# This class is used for keeping track of updates history for reviews
from django_extensions.db.models import TimeStampedModel


class Review(TimeStampedModel):
    content = models.TextField(
        verbose_name="content"
    )
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",  # backwords relation - with this reference we can get all the posts from user
        null=True
    )
    rating_validator = MaxValueValidator(5, message='The rating must be an integer number between 1 and 5.')
    rating = models.DecimalField(
        verbose_name='Rating',
        validators=[rating_validator, ],
        max_digits=1,
        decimal_places=0,
        null=True
    )
    restaurant = models.ForeignKey(
        verbose_name="restaurant",
        to="restaurant.Restaurant",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="review",
        null=True,
        blank=True,
    )

    # created = models.DateTimeField(
    #     verbose_name="created",
    #     auto_now_add=True,
    # )
    # comment = ...
    # M:1 relation with Comment, specified on Comment model

    # review_like = ...
    # M:1 relation with ReviewLike, specified on ReviewLike model

    # TODO! make sure we don't need 'created' field when using ReviewUpdateHistory model

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'  # overwriting defaults
        unique_together = [
            ('restaurant', 'user'),
            # ('review_like', 'user'),
        ]
        # ordering = ["-created"]  # now we dont need to make descending order when calling posts in views

    def __str__(self):
        return self.content[:50]


class ReviewLike(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_review_likes",
        null=True
    )
    review = models.ForeignKey(
        verbose_name="review",
        to="restaurant.Review",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="review_likes",
    )

    class Meta:
        verbose_name = "Review like"
        verbose_name_plural = "Review likes"  # overwriting defaults
        unique_together = [
            ("user", "review"),
        ]


class Restaurant(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_restaurants",
        null=True
    )

    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = CountryField(blank_label='select country')
    zip = models.CharField(
        max_length=9,
        verbose_name='ZIP',
        null=True
    )
    website = models.URLField('Website', max_length=150, null=True)
    # next line is creating validator for regex which will be then used for phone number charfiled.
    # This will make sure that the entered value will follow desired pattern
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)  # validators should be a list
    email = models.EmailField('Email', max_length=70, blank=True)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    category = models.ForeignKey(
        verbose_name='category',
        to='restaurant.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    opening_hours = models.TextField(max_length=100, null=True)

    DEFAULT_STATUS = '$'
    STATUS_CHOICES = [
        (DEFAULT_STATUS, '$'),
        ('low', '$'),
        ('medium', '$$'),
        ('high', '$$$'),
    ]
    status = models.CharField(
        verbose_name='status',
        choices=STATUS_CHOICES,
        default=DEFAULT_STATUS,
        max_length=100,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    #
    # DEFAULT_CAT_NAME = '$'
    # CAT_NAME_CHOICES = [
    #     (DEFAULT_CAT_NAME, '$'),
    #     ('cat_1', '$'),
    #     ('cat_2', '$$'),
    #     ('cat_3', '$$$'),
    # ]
    #
    # category = models.CharField(
    #     verbose_name='category',
    #     choices=CAT_NAME_CHOICES,
    #     default=DEFAULT_CAT_NAME,
    #     max_length=100,
    # )

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comments",
        null=True
    )
    review = models.ForeignKey(
        verbose_name="review",
        to='restaurant.Review',
        on_delete=models.CASCADE,
        related_name="comment",
        null=True
    )
    content = models.TextField(
        verbose_name="content"
    )

    def __str__(self):
        return self.content[:50]


class CommentLike(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comment_likes",
        null=True
    )
    comment = models.ForeignKey(
        verbose_name="comment",
        to="restaurant.Comment",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="comment_likes",
    )

    class Meta:
        verbose_name = "Comment like"
        verbose_name_plural = "Comment likes"  # overwriting defaults
