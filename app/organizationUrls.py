from django.urls import path
from . import views

# import logging
# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug(views.OrganizationList.as_view())

urlpatterns = [
    path('', views.OrganizationList.as_view(), name='organization_list'),
    path('view/<int:pk>', views.OrganizationDetail.as_view(), name='organization_detail'),
    path('new', views.OrganizationCreate.as_view(), name='organization_new'),
    path('edit/<int:pk>', views.OrganizationUpdate.as_view(), name='organization_edit'),
    path('delete/<int:pk>', views.OrganizationDelete.as_view(), name='organization_delete'),
    path('newStudent/<int:pk>', views.StudentCreate.as_view(), name='student_new'),
    path('newOfficer/<int:pk>', views.OfficeCreate.as_view(), name='office_new')
]