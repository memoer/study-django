from django.db import models


class TimeStampedModel(models.Model):
    # auto_now = True       => Models 을 Save를 해줄 때, Date/Time을 기록해준다.
    # auto_now_add = True   => Model을 생성할 때 수시로 업데이트 된다.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # DB 로 생성하진 않는다. ( 해당 TimeStampedModel에 대하여 독립적인 DB Table을 생성해주지 않는다는 것. )
        # 다른 DB에서 상속을 받아 사용하기 위해 설정하는 것.
        abstract = True
