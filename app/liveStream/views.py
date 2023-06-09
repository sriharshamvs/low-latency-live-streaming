from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import LiveStream, ContactDetail, ContactDetailFDP
from .forms import ContactDetailsForm, ContactDetailFdpForm 
import csv

# Create your views here.
def index(request):
    return room(request, 'home')


def export(request, stream_key):
    if not request.user.is_authenticated:
        return redirect('/admin')

    l = LiveStream.objects.filter(stream_key = stream_key)[0]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{stream_key}.csv"'
    if l.collect_details:
        contacts = ContactDetail.objects.filter(live_stream=l).values_list('name','mobile_number','email_address','place').distinct()
        writer = csv.writer(response)
        writer.writerow(['Name', 'Mobile Number', 'Email Address', 'Institution/Place'])
        for cm in contacts:
            writer.writerow(cm)
    elif l.fdp_details:
        contacts = ContactDetailFDP.objects.filter(live_stream=l).values_list('name', 'mobile_number', 'email_address', 'unique_id', 'department', \
         'institute', 'state_of_the_institute', 'country_of_the_institute').distinct()
        writer = csv.writer(response)
        writer.writerow(['name', 'mobile_number', 'email_address', 'unique_id', 'department', \
         'institute', 'state_of_the_institute', 'country_of_the_institute'])
        for cm in contacts:
            writer.writerow(cm)

    

    return response



def room(request, stream_key):
    stream = LiveStream.objects.filter(stream_key=stream_key).all()
    if stream:
        stream = stream[0]
        if stream.collect_details:
            cookie = None
            if 'contact_id' in request.session:
                cookie = request.session['contact_id']
            if request.method == 'GET':
                if not cookie:
                    f = ContactDetailsForm()
                    return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})
                else:
                    contact = ContactDetail.objects.filter(id=cookie)[0]
                    return render(request, 'liveStream/room.html', {'stream': stream, 'contact':contact})

            elif request.method == 'POST':
                f = ContactDetailsForm(request.POST)
                if f.is_valid():
                    c = f.save(commit=False)
                    c.live_stream = stream
                    c.save()
                    request.session['contact_id'] = c.id
                    return render(request, 'liveStream/room.html', {'stream': stream, 'contact':c})
                else:
                    return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})
        elif stream.fdp_details:
            cookie = None
            if 'contact_id' in request.session:
                cookie = request.session['contact_id']
            if request.method == 'GET':
                if not cookie:
                    f = ContactDetailFdpForm()
                    return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})
                else:
                    contact = ContactDetail.objects.filter(id=cookie)[0]
                    return render(request, 'liveStream/room.html', {'stream': stream, 'contact':contact})

            elif request.method == 'POST':
                f = ContactDetailFdpForm(request.POST)
                if f.is_valid():
                    c = f.save(commit=False)
                    c.live_stream = stream
                    c.save()
                    request.session['contact_id'] = c.id
                    return render(request, 'liveStream/room.html', {'stream': stream, 'contact':c})
                else:
                    return render(request, 'liveStream/register.html', {'stream':stream, 'form':f})
        else:
            return render(request, 'liveStream/room.html', {'stream': stream})
    else:
        return HttpResponseNotFound('<h1>Stream Not Found</h1>')
