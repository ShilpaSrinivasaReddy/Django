from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Pyrogasifier, HydrogenBox, GreenHouse, FotoVoltaico, Multimetro, SolarThermal
from django.db.models import Avg, Sum, F
from django.db.models.functions import TruncDate
from django.db.models.functions import ExtractYear
import json


# Create your views here.

def show(request):
    pyro_data = Pyrogasifier.objects.all()
   
    #Use built-in aggregate Django functions
    avg_temp = float(Pyrogasifier.objects.aggregate(Avg('pyro_temperature'))['pyro_temperature__avg'])
    avg_press = float(Pyrogasifier.objects.aggregate(Avg('pyro_pressure'))['pyro_pressure__avg'])
    avg_flow = float(Pyrogasifier.objects.aggregate(Avg('pyro_flow_rate'))['pyro_flow_rate__avg'])

    # Calculate the average values and sum for hydrogen data
    hydro_data = HydrogenBox.objects.all()
    avg_hydrogen_pressure = float(HydrogenBox.objects.aggregate(Avg('hydrogen_pressure'))['hydrogen_pressure__avg'])
    avg_hydrogen_production_rate = float(HydrogenBox.objects.aggregate(Avg('hydrogen_production_rate'))['hydrogen_production_rate__avg'])
    sum_hydrogen_storage_capacity = float(HydrogenBox.objects.aggregate(Sum('hydrogen_storage_capacity'))['hydrogen_storage_capacity__sum'])
    avg_hydrogen_temperature = float(HydrogenBox.objects.aggregate(Avg('hydrogen_temperature'))['hydrogen_temperature__avg'])

    # Calculate the average values for greenhouse data
    greenhouse_data = GreenHouse.objects.all()
    avg_greenhouse_temperature = float(GreenHouse.objects.aggregate(Avg('greenhouse_temperature'))['greenhouse_temperature__avg'])
    avg_greenhouse_humidity = float(GreenHouse.objects.aggregate(Avg('greenhouse_humidity'))['greenhouse_humidity__avg'])
    avg_greenhouse_light_intensity = float(GreenHouse.objects.aggregate(Avg('greenhouse_light_intensity'))['greenhouse_light_intensity__avg'])
    avg_greenhouse_co2_level = float(GreenHouse.objects.aggregate(Avg('greenhouse_co2_level'))['greenhouse_co2_level__avg'])
    avg_par = float(GreenHouse.objects.aggregate(Avg('par'))['par__avg'])

    # Calculate and print the daily averages for FotoVoltaico
    daily_avg_temperatura_pannello = FotoVoltaico.objects.annotate(
        date=TruncDate('datetime_utc')
    ).values('date').annotate(
        avg_temperatura_pannello=Avg('temperatura_pannello')
    ).order_by('date')

    daily_avg_temperatura_ritorno = FotoVoltaico.objects.annotate(
        date=TruncDate('datetime_utc')
    ).values('date').annotate(
        avg_temperatura_ritorno=Avg('temperatura_ritorno')
    ).order_by('date')

    daily_avg_temperatura_mandata = FotoVoltaico.objects.annotate(
        date=TruncDate('datetime_utc')
    ).values('date').annotate(
        avg_temperatura_mandata=Avg('temperatura_mandata')
    ).order_by('date')


    # Calculate the average values for Frequency and total_active_power for each year
    year_avg_frequency = Multimetro.objects.annotate(
        year=ExtractYear('timestamp_utc')
    ).values('year').annotate(
        avg_frequency=Avg('frequency')
    ).order_by('year')

    year_avg_total_active_power = Multimetro.objects.annotate(
        year=ExtractYear('timestamp_utc')
    ).values('year').annotate(
        avg_total_active_power=Avg('total_active_power')
    ).order_by('year')

    # Calculate the average values for solar_energy_production and solar_temperature for each year
    year_avg_solar_energy_production = SolarThermal.objects.annotate(
        year=ExtractYear('weather_datetime_utc')
    ).values('year').annotate(
        avg_solar_energy_production=Avg('solar_energy_production')
    ).order_by('year')

    year_avg_solar_temperature = SolarThermal.objects.annotate(
        year=ExtractYear('weather_datetime_utc')
    ).values('year').annotate(
        avg_solar_temperature=Avg('solar_temperature')
    ).order_by('year')


    print(year_avg_solar_energy_production)
    print(year_avg_solar_temperature)

   
    #print
    context={
        'pyro_data': pyro_data,
        'avg_temp': avg_temp, 
        'avg_press': avg_press,
        'avg_flow': avg_flow, 
        'hydro_data': hydro_data,
        'avg_hydrogen_pressure': avg_hydrogen_pressure,
        'avg_hydrogen_production_rate': avg_hydrogen_production_rate,
        'sum_hydrogen_storage_capacity': sum_hydrogen_storage_capacity,
        'avg_hydrogen_temperature': avg_hydrogen_temperature,
        'greenhouse_data': greenhouse_data,
        'avg_greenhouse_temperature': avg_greenhouse_temperature,
        'avg_greenhouse_humidity': avg_greenhouse_humidity,
        'avg_greenhouse_light_intensity': avg_greenhouse_light_intensity,
        'avg_greenhouse_co2_level': avg_greenhouse_co2_level,
        'avg_par': avg_par,
        'daily_avg_temperatura_pannello': daily_avg_temperatura_pannello,
        'daily_avg_temperatura_ritorno': daily_avg_temperatura_ritorno,
        'daily_avg_temperatura_mandata': daily_avg_temperatura_mandata,
        'year_avg_frequency': year_avg_frequency,
        'year_avg_total_active_power': year_avg_total_active_power,
        'year_avg_solar_energy_production': year_avg_solar_energy_production,
        'year_avg_solar_temperature': year_avg_solar_temperature,
    }
   
    

    return render(request,"show.html", context=context)






