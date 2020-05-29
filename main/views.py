from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import VehicleForm, Profile_Form
from .models import Vehicle, Service, User_Profile, Profile
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile/error.html')
            user_pr.save()
            return render(request, 'profile/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile/create.html', context)

def home(request):
    #vehicles = Vehicle.objects.all()
    #context = {'vehicles': vehicles}
    #return render(request, 'home.html', context)
    # redirect home page
    return HttpResponseRedirect(reverse_lazy('vehicle-list-view'))

@login_required
def ShowUserProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, f'Your account has been been updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/profile.html', context)

def ShowVehicleList(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicle/vehicle_list_view.html', context)

def ShowVehicleDetail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    context = {'operation': 'View', 'vehicle': vehicle}
    return render(request, 'vehicle/vehicle_detail_view.html', context)

@login_required
def UpdateVehicle(request, pk):
    print('UpdateVehicle')
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        print('POST')
        form = VehicleForm(request.POST or None, request.FILES, instance=vehicle)

        if form.is_valid():
            #vehicle.vin = form.cleaned_data["vin"]
            #vehicle.reg_number = form.cleaned_data["reg_number"]
            #vehicle.make = form.cleaned_data["make"]
            #vehicle.model = form.cleaned_data["model"]
            #vehicle.year = form.cleaned_data["year"]
            #vehicle.color = form.cleaned_data["color"]
            #if 'image' in request.FILES:
            #    vehicle.image = form.cleaned_data["image"]
            form.save()
            #vehicle.save()

            print("Save form:" + str(vehicle))
            print(vehicle)
            print(vehicle.imageURL)
            return HttpResponseRedirect(reverse_lazy('vehicle-list-view'))

    else:
        print('REQUEST')
        form = VehicleForm(initial=model_to_dict(vehicle))

    context = {'operation': 'Modify', 'form': form}

    return render(request, 'vehicle/vehicle_update.html', context)

@login_required
def AddVehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            #vehicle = Vehicle.objects.create()
            #vehicle.vin = form.cleaned_data["vin"]
            #vehicle.reg_number = form.cleaned_data["reg_number"]
            #vehicle.make = form.cleaned_data["make"]
            #vehicle.model = form.cleaned_data["model"]
            #vehicle.year = form.cleaned_data["year"]
            #vehicle.color = form.cleaned_data["color"]
            #vehicle.image = form.cleaned_data["image"]
            #vehicle.picture = form.cleaned_data["picture"]
            #vehicle.save()
            form.save()
            #make = form.cleaned_data["make"]
            #model = form.cleaned_data["model"]
            #year = form.cleaned_data("year")
            vin = form.cleaned_data["vin"]
            messages.success(request, f'New vehicle created with VIN #: {vin}!')

            return HttpResponseRedirect(reverse_lazy('vehicle-list-view'))
    else:
        form = VehicleForm()
    context = {'operation': 'Add', 'form': form}

    return render(request, 'vehicle/vehicle_add.html', context)
