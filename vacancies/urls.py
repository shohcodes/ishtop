from django.urls import path
from vacancies import views

urlpatterns = [
    path("", views.get_vacancies, name="vacancies"),
]
