# from django import views
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
# ]

from django.urls import path

from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
