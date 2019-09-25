from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.shortcuts import render, redirect
from .models import Event, Account, Category
from .forms import EventForm, AccountForm
from django.views.generic import CreateView, UpdateView
from users.models import CustomUser
from users.forms import CustomUserChangeForm



class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

# class AccountView(generic.ListView):
#     template_name = 'eventFinderApp/account.html'
#     context_object_name = 'events_list'

#     def get_queryset(self):
#         return Event.objects.filter(host=self.request.user)

def account(request):
    events_list = Event.objects.filter(host=request.user)
    if request.method == 'POST':
        print(request.POST)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    context = {'events_list': events_list, 'form': user_form}
    template_name = 'eventFinderApp/account.html'
    return render(request, template_name, context)


class AddEventCreateView(generic.CreateView):
    # using the create view we can just give it the variables 
    # as the functionaity is already built in!
    form_class = EventForm
    template_name = 'eventFinderApp/addevent.html'
    success_url = reverse_lazy('eventFinderApp:index')
    context_object_name = 'name'


    def form_valid(self, form):
        form.instance.host = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(AddEventCreateView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        initial['host'] = self.request.user.pk
        return initial

# def addevent(request):

#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = EventForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect('/thanks/')
#             form.save()
#             return HttpResponseRedirect(reverse('eventFinderApp:index'))
#         return render(request, 'eventFinderApp/addevent.html', {'eventform': form})
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EventForm()
#         return render(request, 'eventFinderApp/addevent.html', {'eventform': form})

