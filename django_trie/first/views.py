from django.shortcuts import render
# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'items': ['first post', 'second post', 'third post'],
        'obj': {
            'city': 'Minsk',
            'network': 'instagram',
            'color': 'purple'
        }
    }
    return render(request, 'first/index.html', data)


def about(request):
    return render(request, 'first/about.html')
