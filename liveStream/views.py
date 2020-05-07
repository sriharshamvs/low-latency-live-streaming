from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import LiveStream

# Create your views here.
def index(request):
    return render(request, 'liveStream/index.html')

def room(request, stream_key):
    stream = LiveStream.objects.filter(stream_key=stream_key).all()
    if stream:
        return render(request, 'liveStream/room.html', {'stream': stream[0]})
    else:
        return HttpResponseNotFound('<h1>Page Not Found</h1>')