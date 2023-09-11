from .views import *
from django.urls import path


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('aboutipssm', aboutipssm, name='aboutipssm'),
    path('aboutsrinivas', aboutsrinivas, name='aboutsrinivas'),
    path('BBA-Logistics-&-Supply-Chain-Management', logistics, name='logistics'),
    path('BBA-Port-Shipping-Management-&-Logistics', port, name='port'),
    path('BBA - Business Analytics, Entrepreneurship and International Business', business, name='business'),
    path('MBA-Logistics-&-Supply-chain-Management', mba, name='mba'),
    path('contact', contact, name='contact'),
    path('events', events, name='events'),
    path('events/<pk>', eventview, name='eventdetails'),
    path('faculty', faculty, name='faculty'),
    path('gallery', gallery, name='gallery'),
    path('placement', placement, name='placement'),
    path('Faculty-Achivements', tchach, name='tchach'),
    path('Student-Achivements', stdach, name='stdach'),
]