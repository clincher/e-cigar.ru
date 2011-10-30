# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.db import models


class Callback(models.Model):
    site = models.ForeignKey(Site, null=True)
    username = models.CharField(max_length=100, verbose_name=u'Имя')
    phone_number = models.CharField(max_length=30, verbose_name=u'Телефон')

    def __unicode__(self):
        return u'callback from  {site}: {phone_number}, {username}'.format(
            self.__dict__)