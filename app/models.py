from django.db import models
from django.urls import reverse

# Create your models here.

# Student Model


# Organization Model
class Organization(models.Model):
    academic_year = models.CharField(max_length=200, null=False)
    adviser = models.CharField(max_length=200, null=False)
    organization_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.organization_name
    
    def get_absolute_url(self):
        return reverse('organization_edit', kwargs={'pk': self.pk})




    # Office Model
class Office(models.Model):
    firstname = models.ForeignKey(Organization, default=None, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=200, null=False)
    course = models.CharField(max_length=200, null=False)
    email_address = models.CharField(max_length=200, null=False)
    firstname = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    middlename = models.CharField(max_length=200, null=False)
    officer_no = models.CharField(max_length=200, null=False)
    position = models.CharField(max_length=200, null=False)
    year = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.firstname
    def get_absolute_url(self):
        return reverse('office_edit', kwargs={'pk': self.pk})


class Student(models.Model):
    firstname = models.ForeignKey(Organization, default=None, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=200, null=False)
    course = models.CharField(max_length=200, null=False)
    email_address = models.CharField(max_length=200, null=False)
    firstname = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    middlename = models.CharField(max_length=200, null=False)
    student_no = models.CharField(max_length=200, null=False)
    year = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.firstname
    def get_absolute_url(self):
        return reverse('student_edit')#, kwargs={'pk': self.pk})


# Activity Model
class Activity(models.Model):
    #firstname = models.ForeignKey(Office, default=None, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200, null=False)
    date_proposed = models.DateField(auto_now_add=False, auto_now=False)
    description = models.CharField(max_length=200, null=False)
    estimated_budget = models.CharField(max_length=200, null=False)
    #faculty = models.CharField(max_length=200, null=False)
    participant_no = models.CharField(max_length=200, null=False)
    target_participant = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.activity_name
    def get_absolute_url(self):
        return reverse('activity_edit')#, kwargs={'pk': self.pk})

# Report Model
class Report(models.Model):
    #second = models.ForeignKey(Activity, default=None, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=False)
    Poposed_Date = models.DateField(auto_now_add=False, auto_now=False)
    evaluation_report = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('report_edit')#, kwargs={'pk': self.pk})