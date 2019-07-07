from django.urls import path, re_path
from .views import CrearVistaHistoria, detallesDeHistoria

urlpatterns = [
    path('crear_historia/', CrearVistaHistoria, name = 'CrearHistoria'),
    re_path('^verHistoria/(?P<pk>\d+)$', detallesDeHistoria.as_view(), name='detalles-de-historia')
]