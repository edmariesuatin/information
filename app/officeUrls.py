from django.urls import path
from . import views

urlpatterns = [
    path('', views.OfficeList.as_view(), name='office_list'),
    path('view/<int:pk>', views.OfficeDetail.as_view(), name='office_detail'),
    path('new', views.OfficeCreate.as_view(), name='office_new'),
    path('edit/<int:pk>', views.OfficeUpdate.as_view(), name='office_edit'),
    path('delete/<int:pk>', views.OfficeDelete.as_view(), name='office_delete')
]