# Generated by Django 5.1.6 on 2025-03-20 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_hostel_alter_hostelapplication_hostel_name_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelapplication',
            name='year_of_study',
            field=models.CharField(choices=[('Year One', 'Year One'), ('Year Two', 'Year Two'), ('Year Three', 'Year Three'), ('Year Four', 'Year Four'), ('Year Five', 'Year Five'), ('Year Six', 'Year Six')], max_length=20),
        ),
    ]
