from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('spam/', views.spam_predict, name='spam_predict'),
    path('house-rent/', views.house_rent_predict, name='house_rent_predict'),
    path('pension/', views.pension_predict, name='pension_predict'),
    path('logout/', views.logout_view, name='logout'),

]
