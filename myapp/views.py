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

# def book_hostel(request):
#     if request.method == "POST":
#         print("Form submitted!")  # Debugging

#         form = HostelApplicationForm(request.POST)
#         if form.is_valid():
#             print("Form is valid!")  # Debugging
#             application = HostelApplication(
#                 name=form.cleaned_data['name'],
#                 reg_number=form.cleaned_data['reg_number'],
#                 year_of_study=form.cleaned_data['year_of_study'],
#                 gender=form.cleaned_data['gender'],
#                 hostel_type=form.cleaned_data['hostel_type'],
#                 location=form.cleaned_data['location'],
#                 hostel_name=", ".join(form.cleaned_data['hostel_name']),  # Join multiple choices
#                 cost_per_semester=form.cleaned_data['cost_per_semester'],
#                 status="Pending",
#                 user=request.user  
#             )
#             application.save()
#             messages.success(request, "Hostel booking successful! You can view your application status.")
#             return redirect('myapp:my_applications')
#         else:
#             print("Form errors:", form.errors)  # Debugging
#             messages.error(request, "Invalid form submission. Please check the form.")
#     else:
#         form = HostelApplicationForm()
    
#     return render(request, 'book_hostel.html', {'form': form})



# def book_hostel(request):
#     if request.method == "POST":
#         form = HostelApplicationForm(request.POST)
#         if form.is_valid():
#             application = HostelApplication(
#                 name=form.cleaned_data['name'],
#                 reg_number=form.cleaned_data['reg_number'],
#                 year_of_study=form.cleaned_data['year_of_study'],
#                 gender=form.cleaned_data['gender'],
#                 hostel_type=form.cleaned_data['hostel_type'],
#                 location=form.cleaned_data['location'],
#                 hostel_name=", ".join(form.cleaned_data['hostel_name']),  
#                 cost_per_semester=form.cleaned_data['cost_per_semester'],  # Auto-set
#                 status="Pending",
#                 user=request.user  
#             )
#             application.save()
#             messages.success(request, "Hostel booking successful! You can view your application status.")
#             return redirect('myapp:my_applications')
#         else:
#             messages.error(request, "Invalid form submission. Please check the form.")
#     else:
#         form = HostelApplicationForm()
    
#     return render(request, 'book_hostel.html', {'form': form})

# def book_hostel(request):
#     if request.method == "POST":
#         form = HostelApplicationForm(request.POST)
#         if form.is_valid():
#             # Create an instance but don't save yet
#             application = HostelApplication(
#                 user=request.user,  # Set the user
#                 name=form.cleaned_data["name"],
#                 reg_number=form.cleaned_data["reg_number"],
#                 year_of_study=form.cleaned_data["year_of_study"],
#                 gender=form.cleaned_data["gender"],
#                 hostel_type=form.cleaned_data["hostel_type"],
#                 location=form.cleaned_data["location"],
#                 hostel_name=", ".join(form.cleaned_data["hostel_name"]),  # Convert list to string
#                 cost_per_semester=form.cleaned_data["cost_per_semester"],  # Get cost from cleaned data
#             )

#             application.save()  # Now save the instance

#             messages.success(request, "Your hostel application has been submitted successfully!")
#             return redirect("myapp:my_applications")
#         else:
#             messages.error(request, "Invalid form submission. Please check the form.")
#     else:
#         form = HostelApplicationForm()

#     return render(request, "book_hostel.html", {"form": form})



def book_hostel(request):
    if request.method == "POST":
        form = HostelApplicationForm(request.POST)
        if form.is_valid():
            # Get the cleaned form data
            hostel_type = form.cleaned_data["hostel_type"]
            cost_per_semester = form.cleaned_data["cost_per_semester"]

            # Manually set the cost in case it's missing
            if not cost_per_semester:
                cost_per_semester = form.HOSTEL_TYPE_COST.get(hostel_type, 0)

            # Create and save the application
            application = HostelApplication(
                user=request.user,  # Set the user
                name=form.cleaned_data["name"],
                reg_number=form.cleaned_data["reg_number"],
                year_of_study=form.cleaned_data["year_of_study"],
                gender=form.cleaned_data["gender"],
                hostel_type=form.cleaned_data["hostel_type"],
                location=form.cleaned_data["location"],
                hostel_name=", ".join(form.cleaned_data["hostel_name"]),  # Convert list to string
                cost_per_semester=cost_per_semester,  # Set cost explicitly
            )

            application.save()  # Save the instance

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
    applications = HostelApplication.objects.all()

    if request.method == "POST":
        app_id = request.POST.get('accept_application_id')
        decline_id = request.POST.get('decline_application_id')

        if app_id:
            application = HostelApplication.objects.get(id=app_id)
            application.status = "Allocated"
            application.save()
            messages.success(request, f"Application for {application.name} has been accepted.")

        elif decline_id:
            application = HostelApplication.objects.get(id=decline_id)
            application.status = "Declined"
            application.save()
            messages.warning(request, f"Application for {application.name} has been declined.")

    return render(request, 'admin_dashboard.html', {'applications': applications})







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
