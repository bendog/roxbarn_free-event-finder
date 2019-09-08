from django.urls import path
from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/addevent
    path('addevent/', views.addevent, name='addevent'),
    path('addeventview/', views.AddEventView.as_view(), name='addeventview'),
    path('addeventview2/', views.AddEventView2.as_view(), name='addeventview'),
    path('addeventcreateview/', views.AddEventCreateView.as_view(), name='addeventcreateview'),

]