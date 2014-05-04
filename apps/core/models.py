# -*- coding: utf-8 -*-
from django.db import models


class BaseManager(models.Manager):
    def be(self):
        return self.filter(is_delete=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        help_text=u'created time',
        auto_now=True,
        auto_now_add=False)
    updated_at = models.DateTimeField(
        help_text=u'updated time',
        auto_now=True,
        auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True
