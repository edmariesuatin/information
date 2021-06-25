from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActivityList.as_view(), name='activity_list'),
    path('view/<int:pk>', views.ActivityDetail.as_view(), name='activity_detail'),
    path('new', views.ActivityCreate.as_view(), name='activity_new'),
    path('edit/<int:pk>', views.ActivityUpdate.as_view(), name='activity_edit'),
    path('delete/<int:pk>', views.ActivityDelete.as_view(), name='activity_delete')
]
