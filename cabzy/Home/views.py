from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth, Permission
from .forms import RideForm
from .models import ride, Car
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

# Create your views here.
def index(request):
    form = RideForm(request.POST or None)
    if request.method == 'POST':
       form = RideForm(request.POST )
    if form.is_valid():
        instance = form.save(commit = False)
        instance.user = request.user
        instance.car = Car.objects.filter(car_type = instance.car_type)[0]
        
        instance.save()

    context = {

        'form' : form
    }
    return render(request,'index.html', context)

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		username = request.POST['username']

		if User.objects.filter(username = username).exists():
			messages.info(request, 'Username Taken')
			return redirect('/register')
			
		elif User.objects.filter(email = email).exists():
			messages.info(request, 'Email taken')
			return redirect('/register')
		else:		
			user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
			user.save()
			print('user created')
			return HttpResponse("User Created")
	else:
		return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/bookcab')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect(login)
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def bookcab(request):
    
    form = RideForm(request.POST or None)
    if request.method == 'POST':
       form = RideForm(request.POST)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.user = request.user
        instance.car = Car.objects.filter(car_type = instance.car_type).filter(is_available = True)[0]
        instance.completed = False
        instance.save()
        return redirect('/booking')
    context = {

        'form' : form
    }

    return render(request,'bookcab.html', context)

@login_required
def rides(request):
    trav = ride.objects.filter(user = request.user)
    cars = Car.objects.filter(is_running =False)
    return render(request, 'dashboard.html', {'trav': trav, 'cars' : cars})


	
	
@login_required
def booking(request):
    rides = ride.objects.latest('id')
    cars = Car.objects.get(id = rides.car_id)
    return render(request, 'booking.html', {'rides': rides, 'cars' : cars})

    
def cancelride(request):
    rides = ride.objects.latest('id')
    rides.delete()
    return redirect('/bookcab')





def edit(request):
    rides = ride.objects.latest('id')

    if request.method == 'GET':
        return render(request, 'approve.html', {'rides' : rides})
    else:
        x = ride.objects.latest('id')
        y = Car.objects.get(id = x.car_id)
        x.is_approved = request.POST['is_approved']
        
        if x.is_approved == 'approved':
            y.is_available = False
            y.is_running = True
            x.completed = False
            x.save()
            y.save()
            return HttpResponse('DONEDONEDONEDONE')
        y.is_running = request.POST['is_running']

        if y.is_running == request.POST['is_running']:
            x.completed = True
            y.is_available = True
            x.save()
            y.save()  
            return HttpResponse('HAANOK')
        
       

        