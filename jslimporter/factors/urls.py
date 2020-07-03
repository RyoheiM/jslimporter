from django.urls import path
from . import views

app_name = 'factors'

urlpatterns = [
    path('bunchlist/', views.bunchlist, name='bunchlist'),
    path('bunchlist/bunchadd/', views.bunchadd, name='bunchadd'),
    path('bunchlist/<int:pk>/', views.bunchdetail, name='bunchdetail'),
    path('bunchlist/<int:pk>/bunchedit/', views.bunchedit, name='bunchedit'),
]
