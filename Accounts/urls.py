from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]
