# Copyright (c) 2009 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django import template

from apps.banners.models import Banner


register = template.Library()


@register.simple_tag
def banner(slug):
    try:
        banner = Banner.objects.get(slug=slug)
        return '<div class="'+ banner.slug +'">' + banner.body + '</div>'
    except Banner.DoesNotExist:
        return None
