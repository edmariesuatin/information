from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('student/', include('app.studentUrls')),
    path('organization/', include('app.organizationUrls')),
    path('office/', include('app.officeUrls')),
    path('activity/', include('app.activityUrls')),
    path('report/', include('app.reportUrls'))
]
