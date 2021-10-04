from django.urls import path

from personal_info.views import PersonList, PersonCreate, PersonDetail, PersonUpdate, PersonDelete

app_name = 'personal_info'


urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('<int:pk>/', PersonDetail.as_view(), name='person_detail'),
    path('create/', PersonCreate.as_view(), name='person_create'),
    path('<int:pk>/update/', PersonUpdate.as_view(), name='person_update'),
    path('<int:pk>/delete/', PersonDelete.as_view(), name='person_delete'),
]
