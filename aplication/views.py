from django.shortcuts import render, get_object_or_404, redirect
from aplication.models import Booking, Workers, Room

def index(request):
    context = {
        "render_string" : "1Web"
    }
    return render(request, "index.html", context)

def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room_list.html', context)

def worker_list(request):
    workers = Workers.objects.all()
    context = {
        'workers': workers
    }
    return render(request, "worker_list.html", context)

def room_detail(request,pk):
    room = get_object_or_404(Room, pk= pk)
    context = {
        'room': room
    }
    return render(request, 'room_detail.html', context)

def room_list(request):



    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        price = request.POST.get("price")
        room_number = request.POST.get("room_number")

        if name:
            Room.objects.create(name=name, type=type, price=price, room_number=room_number)
            return redirect('room_list')

    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room_list.html', context)

def worker_list(request):



    if request.method == 'POST':
        worker_name = request.POST.get('worker_name')
        worker_id = request.POST.get('type')


        if worker_name:
            Room.objects.create(worker_name=worker_name, worker_id=worker_id)
            return redirect('room_list')

    workers = Room.objects.all()
    context = {
        'worker': workers
    }
    return render(request, 'worker_list.html', context)