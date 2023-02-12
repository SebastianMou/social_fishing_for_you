from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('link_info_instagram/', views.link_info_instagram, name='link_info_instagram'),
    path('link_info_facebook/', views.link_info_facebook, name='link_info_facebook'),

    #pages
    path('instagram/', views.instagram, name='instagram'),
    path('facebook/', views.facebook, name='facebook'),

    # email templates
    path('email_instagram/', views.email_instagram, name='email_instagram'),
]
