from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HostelApplication, Booking, Hostel
from .forms import HostelApplicationForm
from django.contrib.auth.decorators import login_required
from .models import Hostel, HostelApplication, Booking
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from myapp.forms import HostelApplicationForm
from myapp.models import HostelApplication



@staff_member_required
def accept_application(request, application_id):
    application = HostelApplication.objects.get(id=application_id)
    application.status = "Accepted"
    application.save()
    return redirect('admin_dashboard')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HostelApplicationForm
from .models import HostelApplication




def book_hostel(request):
    if request.method == "POST":
        form = HostelApplicationForm(request.POST)
        if form.is_valid():
            application = HostelApplication.objects.create(
                user=request.user, 
                name=form.cleaned_data["name"],
                reg_number=form.cleaned_data["reg_number"],
                year_of_study=form.cleaned_data["year_of_study"], 
                gender=form.cleaned_data["gender"],
                hostel_type=form.cleaned_data["hostel_type"],
                location=form.cleaned_data["location"],
                hostel_name=", ".join(form.cleaned_data["hostel_name"]), 
                cost_per_semester=form.cleaned_data["cost_per_semester"],  
            )

            messages.success(request, "Your hostel application has been submitted successfully!")
            return redirect("myapp:my_applications")
        else:
            messages.error(request, "Invalid form submission. Please check the form.")
    else:
        form = HostelApplicationForm()

    return render(request, "book_hostel.html", {"form": form})




from django.contrib.auth.decorators import login_required

def my_applications(request):
    if not request.user.is_authenticated:
        messages.warning(request, "You must log in to view your applications.")
        return redirect('login_page')  # Redirects to your login page
    
    applications = HostelApplication.objects.filter(user=request.user)
    return render(request, 'my_applications.html', {'applications': applications})


from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser  # Only allow superusers to access



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import HostelApplication

@staff_member_required
def admin_dashboard(request):
    status = request.GET.get('status', 'Pending')  # Default to 'Pending'
    applications = HostelApplication.objects.filter(status=status)

    if request.method == "POST":
        # Handle Accept/Decline actions
        if 'accept_application_id' in request.POST:
            application_id = request.POST.get('accept_application_id')
            application = HostelApplication.objects.get(id=application_id)
            application.status = 'Allocated'
            application.save()
            messages.success(request, f"Application for {application.name} has been accepted.")
        elif 'decline_application_id' in request.POST:
            application_id = request.POST.get('decline_application_id')
            application = HostelApplication.objects.get(id=application_id)
            application.status = 'Declined'
            application.save()
            messages.success(request, f"Application for {application.name} has been declined.")

        return redirect('myapp:admin_dashboard')

    return render(request, 'admin_dashboard.html', {'applications': applications})



from django.contrib import messages

def download_report(request, status):
    valid_statuses = ["Pending", "Confirmed"] 
    if status not in valid_statuses:
        messages.warning(request, f"Invalid status: {status}")
        return redirect('myapp:view_all_bookings')

    bookings = Booking.objects.filter(status=status)

    if not bookings.exists():
        messages.warning(request, f"No {status} bookings found.")
        return redirect('myapp:view_all_bookings')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{status}_bookings.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Hostel', 'Registration Number', 'Gender', 'Status', 'Date Booked'])

    for booking in bookings:
        writer.writerow([
            booking.user.username,
            booking.hostel.name,
            booking.registration_number,
            booking.gender,
            booking.status,
            booking.date_booked.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    return response



@login_required
def view_my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "view_my_bookings.html", {"bookings": bookings})


def home_page(request):
    return render(request, "index.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('myapp:book_hostel')
        else:
            messages.error(request, "Invalid login credentials")
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('myapp:login_page')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                messages.success(request, "Account created successfully.")
                return redirect('myapp:book_hostel')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'accounts/register.html')




from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
import csv

def view_all_bookings(request):
    bookings = Booking.objects.filter(status='Pending')
    return render(request, 'view_all_bookings.html', {'bookings': bookings})

def view_accepted_bookings(request):
    bookings = Booking.objects.filter(status='Allocated')
    return render(request, 'accepted.html', {'bookings': bookings})

def view_declined_bookings(request):
    bookings = Booking.objects.filter(status='Declined')
    return render(request, 'declined.html', {'bookings': bookings})




from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import HostelApplication

def download_filtered_applications_pdf(request, status):
  
    valid_statuses = ["Pending", "Allocated", "Declined"]
    if status not in valid_statuses:
        messages.warning(request, f"Invalid status: {status}")
        return redirect('myapp:admin_dashboard')

    
    applications = HostelApplication.objects.filter(status=status)

    if not applications.exists():
        messages.warning(request, f"No {status} applications found.")
        return redirect('myapp:admin_dashboard')


    buffer = BytesIO()


    pdf = canvas.Canvas(buffer, pagesize=letter)

 
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 750, "Kenyatta University Hostel Applications Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 730, f"Status: {status}")
    pdf.drawString(100, 710, f"Total Applications: {applications.count()}")


    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 680, "Name")
    pdf.drawString(250, 680, "Hostel Name")
    pdf.drawString(400, 680, "Reg. No.")
    pdf.drawString(500, 680, "Status")

    pdf.setFont("Helvetica", 12)
    y = 660
    for application in applications:
        pdf.drawString(100, y, application.name)
        pdf.drawString(250, y, application.hostel_name)
        pdf.drawString(400, y, application.reg_number)
        pdf.drawString(500, y, application.status)
        y -= 20  

   
    pdf.showPage()
    pdf.save()

   
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{status}_applications_report.pdf"'
    return response





from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import HostelApplication

def download_application_report(request, application_id):
    application = HostelApplication.objects.get(id=application_id)

    
    buffer = BytesIO()

    
    pdf = canvas.Canvas(buffer, pagesize=letter)

    
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 750, "Kenyatta University Hostel Application Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 730, f"Dear {application.user.username},")
    pdf.drawString(100, 710, f"This is to confirm that you have applied for {application.hostel_name},")
    pdf.drawString(100, 690, f"which costs KES {application.cost_per_semester} per semester.")
    pdf.drawString(100, 670, "Applications are processed on a first-come, first-served basis.")
    pdf.drawString(100, 650, "However, priority is given to first-year students.")
    pdf.drawString(100, 630, f"Current Status: {application.status}")
    pdf.drawString(100, 610, "Thank you for choosing KU Hostels.")
    pdf.drawString(100, 590, "Best regards,")
    pdf.drawString(100, 570, "KU Hostels Management")

    
    pdf.showPage()
    pdf.save()

    
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{application.hostel_name}_application_report.pdf"'
    return response




from django.shortcuts import render
from .models import HostelApplication

def view_hostel_reports(request):
    if request.method == "POST":
        selected_hostel = request.POST.get("hostel_name")
        print(f"Selected Hostel: {selected_hostel}") 

        applications = HostelApplication.objects.filter(hostel_name=selected_hostel)
        print(f"Applications Found: {applications.count()}")  

        return render(request, "hostel_reports.html", {"applications": applications, "selected_hostel": selected_hostel})
    
    return render(request, "hostel_reports.html")
