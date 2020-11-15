from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


 # here we define the app name,so every time we link the url in html file we have to define with app name
urlpatterns = [
    #path('login/', login,{'template_name': 'authentication/login.html'}, name='login'),  # Django build in class based authentication view,no need to view function,just override url and template in authentication directory
    #path('',views.home,name='home'),
    path('',views.welcome,name='welcome'),
    path('login/',auth_views.LoginView.as_view(),name='login'), # use registration/login.html file, after login it redirect to 'todoapps' means home page which we set into settings.py file
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
