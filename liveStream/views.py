from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import LiveStream, ContactDetail
from .forms import ContactDetailsForm 

# Create your views here.
def index(request):
    return room(request, 'home')

def room(request, stream_key):
    stream = LiveStream.objects.filter(stream_key=stream_key).all()
    if stream:
        stream = stream[0]
        if stream.collect_details:
            if request.method == 'GET':
                f = ContactDetailsForm()
                return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})

            elif request.method == 'POST':
                f = ContactDetailsForm(request.POST)
                if f.is_valid():
                    c = f.save(commit=False)
                    c.live_stream = stream
                    c.save()
                    return render(request, 'liveStream/room.html', {'stream': stream})
                else:
                    return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})
        else:
            return render(request, 'liveStream/room.html', {'stream': stream})
    else:
        return HttpResponseNotFound('<h1>Stream Not Found</h1>')
