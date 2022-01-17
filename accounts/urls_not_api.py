from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.urls import reverse_lazy

from . import views

# app_name='accounts'
urlpatterns = [
    # path('home/', views.index, name='index'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='myapp/login.html')),

    # path('login',views.login_view,name='login'),
    path('register/', views.register,name='register'),
    path('add_user_to_group/<str:username>/',views.add_user_to_group,name="add_user_to_group"),
    # path('users/',views.users,name='users'),
    path('employees/<slug:business_slug>/',views.employeess,name='employees'),

    path('users/delete/<int:id>/', views.delete_user, name='user_delete'),
    # path('logout_view/',views.logout_view, name='logout_view'),
    path('resetPassword/<int:id>/', views.resetPassword, name='resetPassword'),


    path('deactivate_activate_user/<int:id>/',views.deactivate_activate_user,name='deactivate_activate_user'),




    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),

    path('change_password/',
        auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'),name='change_password'),

    path('password_reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',success_url=reverse_lazy('index')),name='password_reset_confirm',
    ),
    path('password_change_done/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done',),

   
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_done',),

    path('check_default_password/',views.check_default_password,name='check_default_password'),
    path('reset_password/<int:user>/', views.resetPassword, name='resetPassword'),

    path('hello/', views.HelloView.as_view(), name='hello'),

]
