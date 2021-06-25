from django.contrib import admin
from .models import Student, Office, Organization, Activity, Report

admin.site.register(Organization)
admin.site.register(Office)
admin.site.register(Student)
admin.site.register(Activity)
admin.site.register(Report)

# admin.site.register()
# Register your models here.
