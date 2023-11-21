from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    country_name = models.CharField(db_column='Country_name', primary_key=True, max_length=255)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=9, decimal_places=6)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=9, decimal_places=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Finance(models.Model):
    data = models.DateField(db_column='Data', primary_key=True)  # Field name made lowercase.
    risparmio_energetico = models.FloatField(db_column='Risparmio_Energetico', blank=True, null=True)  # Field name made lowercase.
    generazione_elettrica = models.FloatField(db_column='Generazione_Elettrica', blank=True, null=True)  # Field name made lowercase.
    ricavi = models.FloatField(db_column='Ricavi', blank=True, null=True)  # Field name made lowercase.
    spese = models.FloatField(db_column='Spese', blank=True, null=True)  # Field name made lowercase.
    utile_netto = models.FloatField(db_column='Utile_Netto', blank=True, null=True)  # Field name made lowercase.
    ritorno_sull_investimento = models.FloatField(db_column='Ritorno_sull_Investimento', blank=True, null=True)  # Field name made lowercase.
    spesa_di_ammortamento = models.FloatField(db_column='Spesa_di_Ammortamento', blank=True, null=True)  # Field name made lowercase.
    tasse_pagate = models.FloatField(db_column='Tasse_Pagate', blank=True, null=True)  # Field name made lowercase.
    flusso_di_cassa_netto = models.FloatField(db_column='Flusso_di_Cassa_Netto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finance'


class FotoVoltaico(models.Model):
    datetime_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='datetime_utc', primary_key=True)
    solarimetro = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stato_01 = models.CharField(max_length=255, blank=True, null=True)
    temperatura_mandata = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura_pannello = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura_ritorno = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'foto_voltaico'


class FotoVoltaicoFinance(models.Model):
    datetime_utc = models.OneToOneField(FotoVoltaico, models.DO_NOTHING, db_column='datetime_utc', primary_key=True)
    plant_name = models.CharField(max_length=255, blank=True, null=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foto_voltaico_finance'


class GreenHouse(models.Model):
    greenhouse_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    greenhouse_humidity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    greenhouse_light_intensity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    greenhouse_co2_level = models.DecimalField(db_column='greenhouse_CO2_level', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    greenhouse_start_time = models.DateTimeField(blank=True, null=True)
    greenhouse_end_time = models.DateTimeField(blank=True, null=True)
    weather_datetime_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='weather_datetime_utc', primary_key=True)
    par = models.DecimalField(db_column='PAR', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'green_house'


class HydrogenBox(models.Model):
    hydrogen_production_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hydrogen_storage_capacity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hydrogen_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hydrogen_pressure = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hydrogen_start_time = models.DateTimeField(blank=True, null=True)
    hydrogen_end_time = models.DateTimeField(blank=True, null=True)
    weather_datetime_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='weather_datetime_utc', primary_key=True)

    class Meta:
        managed = False
        db_table = 'hydrogen_box'


class Multimetro(models.Model):
    phase_current_l1 = models.DecimalField(db_column='phase_current_L1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    phase_current_l2 = models.DecimalField(db_column='phase_current_L2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    phase_current_l3 = models.DecimalField(db_column='phase_current_L3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    frequency = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_active_power = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    active_power_l1 = models.DecimalField(db_column='active_power_L1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    active_power_l2 = models.DecimalField(db_column='active_power_L2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    active_power_l3 = models.DecimalField(db_column='active_power_L3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l1_l2 = models.DecimalField(db_column='line_voltage_L1_L2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l1_n = models.DecimalField(db_column='line_voltage_L1_N', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l2_l3 = models.DecimalField(db_column='line_voltage_L2_L3', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l2_n = models.DecimalField(db_column='line_voltage_L2_N', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l3_l1 = models.DecimalField(db_column='line_voltage_L3_L1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    line_voltage_l3_n = models.DecimalField(db_column='line_voltage_L3_N', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    timestamp_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='timestamp_utc', primary_key=True)

    class Meta:
        managed = False
        db_table = 'multimetro'


class Pyrogasifier(models.Model):
    pyro_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pyro_pressure = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pyro_flow_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pyro_start_time = models.DateTimeField(blank=True, null=True)
    pyro_end_time = models.DateTimeField(blank=True, null=True)
    weather_datetime_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='weather_datetime_utc', primary_key=True)

    class Meta:
        managed = False
        db_table = 'pyrogasifier'


class SampleWeatherData(models.Model):
    datetime_utc = models.TextField(blank=True, null=True)
    temperatura_2m = models.TextField(blank=True, null=True)
    umidita_relativa = models.TextField(blank=True, null=True)
    velocita_vento_10m = models.TextField(blank=True, null=True)
    precipitazioni = models.TextField(blank=True, null=True)
    bni = models.TextField(blank=True, null=True)
    dhi = models.TextField(blank=True, null=True)
    ghi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_weather_data'


class SolarThermal(models.Model):
    solar_collector_area = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solar_efficiency = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solar_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solar_energy_production = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    solar_start_time = models.DateTimeField(blank=True, null=True)
    solar_end_time = models.DateTimeField(blank=True, null=True)
    weather_datetime_utc = models.OneToOneField('WeatherInfo', models.DO_NOTHING, db_column='weather_datetime_utc', primary_key=True)

    class Meta:
        managed = False
        db_table = 'solar_thermal'


class WeatherInfo(models.Model):
    datetime_utc = models.DateTimeField(primary_key=True)
    temperatura_2m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    umidita_relativa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    velocita_vento_10m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    precipitazioni = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bni = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dhi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ghi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_info'