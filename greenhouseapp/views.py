from django.shortcuts import render
from django.http import JsonResponse
from .models import GreenhouseData
from django.utils import timezone


# Create your views here.
# http://127.0.0.1:8000/chart_data/?bim=15&temperature=16&spo2=18&strick=20&bp=16
def chart_data_view(request):
    moisture1 = request.GET.get('moisture1', None)
    moisture2 = request.GET.get('moisture2', None)
    temperature1 = request.GET.get('temperature1', None)
    temperature2 = request.GET.get('temperature2', None)
    humidity1 = request.GET.get('humidity1', None)
    humidity2 = request.GET.get('humidity2', None)

    # Create a dictionary to store the data you want to save
    data_to_save = {
        'timestamp': timezone.now(),
        'moisture1': moisture1,
        'moisture2': moisture2,
        'temperature1': temperature1,
        'temperature2': temperature2,
        'humidity1': humidity1,
        'humidity2': humidity2,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    GreenhouseData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})

def display_chart_data(request):
    greenhouse_data = GreenhouseData.objects.all()
    return render(request, 'greenhouseapp/dashboard_view.html', {'greenhouse_data': greenhouse_data})

def add_temp(request):
    greenhouse_data = GreenhouseData.objects.all()
    latest_entry = greenhouse_data.latest('timestamp')
    return render(request, 'greenhouseapp/add_temperature.html', {'greenhouse_data': greenhouse_data,'latest_entry': latest_entry})
