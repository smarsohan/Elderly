# Generated by Django 4.0.6 on 2022-08-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_workdone_alter_confirmedappointment_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('nurse_name', models.CharField(default=None, max_length=100)),
                ('image', models.ImageField(null=True, upload_to='Images/Nurses')),
                ('service_name', models.CharField(max_length=100)),
                ('service_price', models.CharField(max_length=100)),
                ('service_area', models.CharField(max_length=100)),
                ('booking_time', models.CharField(max_length=100)),
                ('total', models.CharField(default=None, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Patient Appointment',
            },
        ),
    ]
