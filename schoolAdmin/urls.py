from django.urls import path
from . import views


urlpatterns=[
    path('home',views.schooladmin_home),
    path('viewstaff',views.view_staff), 
    path('addstaff',views.add_staff),
    path('viewstudent',views.view_student),
]
