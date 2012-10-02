#-*- coding=utf8 -*-
'''
Created on 16.06.2012

@author: jskonst
'''
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import settings
def home(request):
    staticfile=settings.STATIC_ROOT+"info.html"
    info=open(staticfile)
    text=info.read()
    info.close()
    return render_to_response('test.html',{'content':text},RequestContext(request))