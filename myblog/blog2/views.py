from django.shortcuts import render
from django.http import HttpResponse

# Django中所有的请求都用函数处理

def index(request):
    return render(request, 'blog2/index.html')