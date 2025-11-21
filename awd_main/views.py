import time

from django.http import HttpResponse
from django.shortcuts import render

from dataentry.task import celery_test_task

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    #I want to execute a time consuming task here
    celery_test_task.delay()
    return HttpResponse('<h3>Function executed successfull</h3>')