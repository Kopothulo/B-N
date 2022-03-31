from django.urls import path
from .import  views

urlpatterns=[

     path('',                  views.index,                          name='index'),
     path('logout/',           views.logout_view,                    name='logout'),
     path('login/',            views.login_request,                  name='login'),
     path('register/',         views.customer_register.as_view(),    name='register'),
     path('home/',             views.Homes,                          name='home'),
     path('hotel/',            views.Hotels,                         name='hotel'),
     path('cottage/',          views.Cottages,                       name='cottage'),
     path('rooms/',            views.AllRooms,                       name='rooms'),
     path('room',              views.RoomDetails,                    name='room'),
     path('dasboard',          views.Dasboard,                       name='receptionist'),

    
]