# -*- coding: utf-8 -*-
from core.utils import template_response

# from . import api


@template_response('base.html')
def some_view(request):
    return {}
