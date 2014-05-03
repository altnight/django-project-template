# -*- coding: utf-8 -*-
from django.db import models

from core.models import BaseModel, BaseManager
# from django.contrib.auth.models import User


class {{ app_name|title }}(BaseModel):
    """
    """

    def __unicode__(self):
        return u'<%s> id=%s' % (self.__class__, self.id)

    class Meta:
        db_table = u'{{ app_name }}'
        verbose_name = u"{{ app_name}}"
        ordering = ['-id']
