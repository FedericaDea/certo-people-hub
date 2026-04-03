from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aggiorna-stato/<int:richiesta_id>/', views.aggiorna_stato, name='aggiorna_stato'),
    path("dashboard/", views.dashboard, name="dashboard"),
]