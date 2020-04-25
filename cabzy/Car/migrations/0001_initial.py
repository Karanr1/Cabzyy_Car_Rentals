# Generated by Django 3.0.4 on 2020-04-24 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=200)),
                ('car_number', models.CharField(max_length=200)),
                ('car_type', models.CharField(choices=[('mini', 'mini'), ('micro', 'micro'), ('sedan', 'sedan')], default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('mini', 'mini'), ('micro', 'micro'), ('sedan', 'sedan')], default='sedan', max_length=200)),
                ('car_pickup', models.CharField(choices=[('NHR', 'NHR'), ('AZD', 'AZD'), ('LBS', 'LBS')], default='AZD', max_length=200)),
                ('car_drop', models.CharField(choices=[('NHR', 'NHR'), ('AZD', 'AZD'), ('LBS', 'LBS')], default='LBS', max_length=200)),
                ('is_approved', models.CharField(choices=[('approved', 'approved'), ('denied', 'denied'), ('not Confirmed', 'not Confirmed')], default='not confirmed', max_length=200)),
                ('cab', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Car.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Car.Car_location'),
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
