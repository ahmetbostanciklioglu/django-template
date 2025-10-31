from django.shortcuts import render, HttpResponse


def blog_view(request):
    return HttpResponse("This is a blog page view")


