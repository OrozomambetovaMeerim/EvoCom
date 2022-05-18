from django.urls import path
from main.views import About_UsListAPIView, Choose_UsListAPIView, Our_ServicesListAPIView,ServicesListAPIView,PartnersListAPIView, ContactsListAPIView


urlpatterns = [
    path('', About_UsListAPIView.as_view(), name='about_us-list'),
    path('choose_us/', Choose_UsListAPIView.as_view(), name='choose_us-list'),
    path('our_services/', Our_ServicesListAPIView.as_view(), name='our_services-list'),
    path('services/', ServicesListAPIView.as_view(), name='services-list'),
    path('partners/', PartnersListAPIView.as_view(), name='partners-list'),
    path('contacts/', ContactsListAPIView.as_view(), name='contacts-list'),
]