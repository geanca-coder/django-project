from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Python"},
    {'id': 2, 'name': "Django"},
    {'id': 3, 'name': "FastAPI"},
    {'id': 4, 'name': "Docker"},
    {'id': 5, 'name': "Kubernetes"}
]


def home(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i 
    context = {'room': room}
    return render(request, 'base/room.html', context)