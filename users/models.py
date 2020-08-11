from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "othter"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # null은 DB에서 사용되는 것이고, blank는 form에서 required인 지 확인하는 것.
    avatar = models.ImageField(blank=True)
    # choices -> DB에 직접 영향을 주진 않는다, Form에 변화를 준 것뿐
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # Text 는 blank = True를 해도 좋다 -> "" 로 저장된다.
    bio = models.TextField(blank=True)
    # Date 는 blank = True로 하면 안됨 -> blank일 경우, NULL 을 넣어주어야 한다 ("" 저장 X)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
