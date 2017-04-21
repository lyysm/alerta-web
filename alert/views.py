# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib2
import json, time

from django.shortcuts import render

# alert-list
def alert(request):
    return render_to_response('alert/alert.html')

# top10
def top10(request):
    return render_to_response('alert/top10.html')


# details
def details(request):
    return render_to_response('alert/top10.html')


# users
def users(request):
    return render_to_response('alert/users.html')


# about
def about(request):
    # status
    status_result = urllib2.urlopen('http://127.0.0.1:8080/management/status').read()
    data = json.loads(status_result)
    # 版本信息
    api = data['application'] + "-" + data['version']
    # 秒数转换成时间
    minutes, seconds = divmod(data['uptime']/1000, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours =  divmod(hours, 24)
    up_time = "%d天%02d小时%02d分%02d秒" % (days, hours, minutes, seconds)
    # 当前时间
    app_time = time.localtime(data['time']/1000)
    now = time.strftime('%Y-%m-%d %H:%M:%S', app_time)
    manifest_result = urllib2.urlopen('http://127.0.0.1:8080/management/manifest').read()
    print manifest_result
    info = json.loads(manifest_result)
    build = info['alerta']['build']
    print data['metrics']
    for i in data:
        print i
        print data.keys()
    return render(request, 'alert/about.html', {'api':api, 'build':build, 'now':now, 'uptime':up_time, 'data': data['metrics']})