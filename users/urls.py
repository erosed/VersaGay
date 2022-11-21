from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/nuevogasto/', views.NuevoGastoView, name="nuevogasto"),
    path('profile/<username>/vergastos/', views.vergasto, name="vergastos"),
    path('profile/<username>/vergastos/subirgasto/', views.subirgasto, name="subirgasto"),
    path('vergastos/<int:pk>/',views.borrarlink, name="borrarlink"),
]