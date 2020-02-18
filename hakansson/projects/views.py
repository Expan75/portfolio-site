from django.shortcuts import render, HttpResponse

# Create your views here.
def listProjectsView(request):
    return HttpResponse('Hello from listProjectsView!')