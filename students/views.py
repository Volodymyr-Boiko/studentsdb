from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


def students_list(request):
    return render(request, 'students_list.html', {})