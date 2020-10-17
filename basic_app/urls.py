from django.urls import path
from basic_app import views

app_name = 'basic_app'
urlpatterns= [
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other'),
    path('register',views.register,name='register'),
    path('logout',views.user_logout,name='logout'),
    path('special',views.special,name='special'),
    path('user_login',views.user_login,name='user_login'),
]
