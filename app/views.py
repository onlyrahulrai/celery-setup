from django.shortcuts import HttpResponse
from app.tasks import add

# Create your views here.

def home(request):
    add.delay(2,3)
    return HttpResponse("App Folder")