from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('book/', views.book_hostel, name='book_hostel'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('view-my-bookings/', views.view_my_bookings, name='view_my_bookings'),
    path('book-hostel/', views.book_hostel, name='book_hostel'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('accept-application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('view-all-bookings/', views.view_all_bookings, name='view_all_bookings'),
    path('view-accepted-bookings/', views.view_accepted_bookings, name='view_accepted_bookings'),
    path('view-declined-bookings/', views.view_declined_bookings, name='view_declined_bookings'),
    path('download-report/<str:status>/', views.download_report, name='download_report'),
    path('download-application-report/<int:application_id>/', views.download_application_report, name='download_application_report'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
