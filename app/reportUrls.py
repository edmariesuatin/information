from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportList.as_view(), name='report_list'),
    path('view/<int:pk>', views.ReportDetail.as_view(), name='report_detail'),
    path('new', views.ReportCreate.as_view(), name='report_new'),
    path('edit/<int:pk>', views.ReportUpdate.as_view(), name='report_edit'),
    path('delete/<int:pk>', views.ReportDelete.as_view(), name='report_delete')
]