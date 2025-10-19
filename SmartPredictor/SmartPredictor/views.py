from django.contrib import admin
from django.urls import path, include
from predictions import views  
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # dashboard page
    path('predict/spam/', views.spam_predict, name='spam_predict'),
    path('predict/house/', views.house_predict, name='house_predict'),
    path('predict/pension/', views.pension_predict, name='pension_predict'),
]
