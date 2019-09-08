from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


def account(request):
    return render(request, 'eventFinderApp/account.html')


# the fucntional view for add event
def addevent(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        eventform = EventForm(request.POST)
        # check whether it's valid:
        if eventform.is_valid():
            # save the data from the form
            eventform.save()
            # redirect to the event list
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
    # create the context for our template
    context = {'eventform': eventform}
    # build the response with our template
    template = 'eventFinderApp/addevent.html'
    return render(request, template, context)


# the Class based view for add event
class AddEventView(generic.View):

    # in the class basded view we handle the GET request with a get() function
    def get(self, request):
        # create our form instance
        eventform = EventForm()
        # assign it to the context
        context = {'eventform': eventform}
        # return our template with our context
        template = 'eventFinderApp/addevent.html'
        return render(request, template, context)

    # in the class based view we handle the POST request with a post() function
    def post(self, request):
        # we create our form instance with the data from the request
        eventform = EventForm(request.POST)
        # check if the form is valid
        if eventform.is_valid():
            # save the data of the form
            eventform.save()
            # redirect to the list of events 
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        # if the form isn't valid return the form (with automatic errors)
            # create the context for our template
        context = {'eventform': eventform}
        # build the response with our template
        template = 'eventFinderApp/addevent.html'
        return render(request, template, context)


# there's a lot of duplicated lines in our AddEventView so lets try and fix that
# this class is exactly the same as the one above!
# it just is arranged a little differently
class AddEventView2(generic.View):

    template = 'eventFinderApp/addevent.html'
    form_class = EventForm
    success_url = reverse_lazy('eventFinderApp:index')
    # we have to use reverse_lazy so that urls.py can load our class
    # and not get stuck in a recursive loop 

    def form_context(self, eventform):
        # assign the form to the context
        return {'eventform': eventform}

    # in the class basded view we handle the GET request with a get() function
    def get(self, request):
        # create our form instance
        eventform = self.form_class()
        # return our template with our contex
        return render(request, self.template, self.form_context(eventform))

    # in the class based view we handle the POST request with a post() function
    def post(self, request):
        # we create our form instance with the data from the request
        eventform = self.form_class(request.POST)
        # check if the form is valid
        if eventform.is_valid():
            # save the data of the form
            eventform.save()
            # redirect to the list of events 
            return HttpResponseRedirect(self.success_url)
        # if the form isn't valid return the form (with automatic errors)
        # build the response with our template
        return render(request, self.template, self.form_context(eventform))


