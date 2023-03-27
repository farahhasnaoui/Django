from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic import ListView,DetailView
from .forms import*
# Create your views here.
#Views funtion based
def HomePage(request):
    return HttpResponse('<h1>Hello from home page</h1>')

def ListEvent(request):
    list =Event.objects.all()
    return render(request,'events/EventList.html' , {'events' : list})



def add_event(req):

    form = EventForm()
    if req.method == "POST":
        form = EventForm(req.POST,req.FIELDS)
        if form.is_valid:
            print(**form.cleaned_data)
            Event.objects.create(**form.cleaned_data)
        else:
            print(form.errors)    

    return render(req, "events/event_form.html",{'form':form})

#Views Class Based

class ListEventView(ListView):
    model =Event
    template_name ="events/EventList.html"
    context_object_name ="events"

# retour personalisé
    
def ListEvents(request):
    list =Event.objects.filter(state = True)
    return render(request,'events/Listevent.html' , {'events' : list})



class ListEventView(ListView):
    model =Event
    template_name ="events/Listevent.html"
    context_object_name ="events"
    def get_queryset(self) :
        return Event.objects.filter(state=True)

class DetailEventView(DetailView):

    model=Event
    template_name ="events/DetailsEvent.html"
    context_objects_name ="event"







