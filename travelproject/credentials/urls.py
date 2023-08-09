from . import views
from django . urls import path
urlpatterns=[
    path('register',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]