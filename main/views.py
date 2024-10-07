from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Head page of us market',
        'nums': ['first', 'second'],
        'dict': {'name': 'Bob'},
        'is_authenticated': True,
    } 
    
    return render(
        request=request,
        template_name='main/index.html',
        context=context
                  )

def about(request):
    return HttpResponse('About page')


