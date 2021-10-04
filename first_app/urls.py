

from django.urls import path

from first_app.views import TestIndex

app_name = 'first_app'

urlpatterns = [
    path('<int:num>/', TestIndex.as_view(), name='index'),
]
