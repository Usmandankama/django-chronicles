from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
def blog(request):
    return HttpResponse("This is the blog page.")

def chat(request):
    return HttpResponse("This is the chat page.")