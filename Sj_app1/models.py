from django.db import models


class FeedBack(models.Model):

    objects: models.QuerySet
    
    quality = models.IntegerField("商品质量", default=1)
    attitude = models.IntegerField("客服态度", default=1)
    speed = models.IntegerField("物流速度", default=1)
    comment = models.TextField("评价内容", default="", max_length=260, blank=True)  # blank 允许为空
    anonymous = models.BooleanField("是否匿名", default=False)
