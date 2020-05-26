from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import VehicleForm, Profile_Form
from .models import Vehicle, Service, User_Profile
from django.urls import reverse_lazy

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
    return HttpResponseRedirect(reverse_lazy('vehicle-list-view'))

def ShowVehicleList(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicle/vehicle_list_view.html', context)

def ShowVehicleDetail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    context = {'operation': 'View', 'vehicle': vehicle}
    return render(request, 'vehicle/vehicle_detail_view.html', context)

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

def AddVehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = Vehicle.objects.create()
            vehicle.vin = form.cleaned_data["vin"]
            vehicle.reg_number = form.cleaned_data["reg_number"]
            vehicle.make = form.cleaned_data["make"]
            vehicle.model = form.cleaned_data["model"]
            vehicle.year = form.cleaned_data["year"]
            vehicle.color = form.cleaned_data["color"]
            vehicle.image = form.cleaned_data["image"]
            vehicle.save()

            return HttpResponseRedirect(reverse_lazy('vehicle-list-view'))
    else:
        form = VehicleForm()
    context = {'operation': 'Add', 'form': form}

    return render(request, 'vehicle/vehicle_add.html', context)
