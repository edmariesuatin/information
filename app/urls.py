from django.urls import path
from . import views

urlpatterns = [
	#path('home', views.homepage, name="home"),
	#path('', views.StudentList.as_view(), name='student_list')
	path('', views.OrganizationList.as_view(), name='organization_list'),
]
