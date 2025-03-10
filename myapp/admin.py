from django.contrib import admin
from .models import Hostel, Booking, HostelApplication

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "hostel_type", "available_spaces", "capacity")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "hostel", "gender", "registration_number", "date_booked", "status")

@admin.register(HostelApplication)
class HostelApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "hostel_name", "status", "year_of_study", "cost_per_semester")
