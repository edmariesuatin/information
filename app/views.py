from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import json
from django.core import serializers
from django.utils import timezone

from .models import Student, Office, Organization, Activity, Report

# Create your views here.

#Help Me Lord huhuu

def homepage(request):

    return render(request,'home.html')


    '''

def org(request):

        if request.method == 'POST':

        Organization = Organization.objects.create()
        Organization.objects.create(
            org_name = request.POST['org_name'],
            academic_year = request.POST['academic_year'],
            adviser = request.POST['adviser'],
            )

        return redirect('organization.html')
        
        em = Mainpage()
        organization = request.POST['organization'],
        position = request.POST['position']
        em.save()

        return render(request,'organization.html')

def member(request):

    if request.method == 'POST':

        organization = MainPage.objects.create()
        Mainpage.objects.create(
            organization = request.POST['organization'],
            position = request.POST['position'],
            )

        return redirect('Contibute')
        
        em = Mainpage()
        organization = request.POST['organization'],
        position = request.POST['position']
        em.save()
    return render(request,'dual.html')

# Create your views here.
def officer(request):

    return render(request,'activities.html')

def report(request):
    
    #em = Mainpage.objects.all().order_by('classification')
    return render(request,'reports.html')'''


# Create your views here.
def play(request):

    return render(request,'home.html')



# Student Views
class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = ['contact_number', 'course', 'email_address', 'firstname', 'gender', 'lastname', 'middlename', 'student_no', 'year']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['contact_number', 'course', 'email_address', 'firstname', 'gender', 'lastname', 'middlename', 'student_no', 'year']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


# Organization Views
class OrganizationList(ListView):
    model = Organization
 
class OrganizationDetail(DetailView):
    model = Organization

class OrganizationCreate(CreateView):

    model = Organization
    fields = ['academic_year', 'adviser', 'organization_name']
    # fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('organization_list')

class OrganizationUpdate(UpdateView):
    model = Organization

    fields = ['academic_year', 'adviser', 'organization_name']
    success_url = reverse_lazy('organization_list')

class OrganizationDelete(DeleteView):
    model = Organization
    success_url = reverse_lazy('organization_list')


# Office Views
class OfficeList(ListView):
    model = Office

class OfficeDetail(DetailView):
    model = Office

class OfficeCreate(CreateView):

    model = Office
    fields = ['contact_number', 'course', 'email_address', 'firstname', 'gender', 'lastname', 'middlename', 'officer_no', 'position', 'year']
    success_url = reverse_lazy('office_list')

    

class OfficeUpdate(UpdateView):
    model = Office
    fields = ['contact_number', 'course', 'email_address', 'firstname', 'gender', 'lastname', 'middlename', 'officer_no', 'position', 'year']
    success_url = reverse_lazy('office_list')

class OfficeDelete(DeleteView):
    model = Office
    success_url = reverse_lazy('office_list')


# Activity Views
class ActivityList(ListView):
    model = Activity

class ActivityDetail(DetailView):
    model = Activity

class ActivityCreate(CreateView):
    model = Activity
    fields = ['activity_name', 'date_proposed', 'description', 'estimated_budget', 'participant_no', 'target_participant']
    success_url = reverse_lazy('report_form')

class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['activity_name', 'date_proposed', 'description', 'estimated_budget', 'participant_no', 'target_participant']
    success_url = reverse_lazy('report_form')


class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('activity_list')


# Report Views
class ReportList(ListView):
    model = Report

class ReportDetail(DetailView):
    model = Report

class ReportCreate(CreateView):
    model = Report
    fields = ['description', 'evaluation_report', 'status', 'Poposed_Date']
    success_url = reverse_lazy('report_list')

class ReportUpdate(UpdateView):
    model = Report
    fields = ['description', 'evaluation_report', 'status']
    success_url = reverse_lazy('report_list')

class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('report_list')

