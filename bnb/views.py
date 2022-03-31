from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .decorators import unauthenticated_user    
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, ReseptionistSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *

#========================================================== system operation(s) ========================================
def register(request):
    return render(request, 'bnb/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'bnb/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class employee_register(CreateView):
    model = User
    form_class = ReseptionistSignUpForm
    template_name = 'bnb/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashbaord')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                try:
                    login(request, user)
                    return redirect('dashboard')
                except:
                    pass    
            elif user is not None and user.is_customer:
                try:
                    login(request, user)
                    return redirect('index')
                except:
                    pass
        else:
            messages.info(request,"Invalid username or password")
    context={'form':AuthenticationForm()}
    return render(request, 'bnb/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')



def index (request, pk = None):
    context={}
    return render(request, 'bnb/index.html',context)


def Booking (request, pk = None):
    context={}
    return render(request, 'bnb/room_deatils.html',context)

def Contactings(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={'form':form}
    return render(request, 'bnb/index.html', context)


#=================================================================== END ===============================================











#======================================================== BnB room categories ===========================================

def Hotels(request):
    hotel = Room.objects.filter(rental_type="Hotel")
    context={ 'hotel':hotel}
    return render(request, 'bnb/hotel.html',context)


def Homes(request):
    homes = Room.objects.filter(rental_type="Home")
    context={'homes':homes}
    return render(request, 'bnb/home.html',context)


def Cottages(request):
    cottage = Room.objects.filter(rental_type="Cottage")
    context={'cottage':cottage}
    return render(request, 'bnb/cottage.html',context)


#==========================================================  END ========================================================



def AllRooms(request):
    r = Room.objects.all()
    context={'r':r}
    return render(request, 'bnb/all_rooms.html',context)

def RoomDetails(request):
    context={}
    return render(request, 'bnb/room_details.html',context)

#@login_required
def Dasboard(request):
    context={}
    return render(request, 'bnb/dashboard.html',context)







"""""  
def confirm(request, pk = None):
    form = ReservstionForm
    if request.method == 'POST':
        if pk:
            invalid_dates = False
            #get the room 
            room = Room.objects.get(pk = pk)
            Guest_id  = request.user
            check_in  = request.session['check_in'] 
            check_out = request.session['check_out']

            # check wether the dates are valid
            # case 1: a room is booked before the check_in date, and checks out after the requested check_in date
            case_1 = reservation.objects.filter(room=room, check_in__lte=check_in, check_out__gte=check_in).exists()

            # case 2: a room is booked before the requested check_out date and check_out date is after requested check_out date
            case_2 = reservation.objects.filter(room=room, check_in__lte=check_out, check_out__gte=check_out).exists()
            
            case_3 = reservation.objects.filter(room=room, check_in__gte=check_in, check_out__lte=check_out).exists()

            if case_1 or case_2 or case_3:
                   messages.info(request,"This room is not available on your selected dates")                  
            else:
                form = ReservstionForm(request.POST)
                if form.is_valid():
                    form.save()
                return redirect('customer')
    context={'form':form}
    return render(request, 'boroko/index.html',context)
 
"""