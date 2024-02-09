from django.urls import path
from .views import login_view, administration, administration_dashboard

urlpatterns = [
    path('', login_view, name='login'),
    path('administration_if/', administration, name='administration'),
    path('administration/dashboard/', administration_dashboard, name='administration_dashboard'),
    # Altri URL del tuo progetto...
]