from django.shortcuts import render, HttpResponse


def myapp_view(request):
    return HttpResponse("This is a blog page view")


