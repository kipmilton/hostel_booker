# Generated by Django 5.1.6 on 2025-02-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Allocated', 'Allocated')], default='Pending', max_length=20),
        ),
    ]
