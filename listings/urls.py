from django.urls import path
from . import views

urlpatterns = [
    # /listings için de listings appindeki views.pyda index fonksiyonu oluşturulacak
    path('', views.index, name='listings'),
    # /listings/23 gibi spesifik bir listing i göstermek için aşağıdaki gibi path
    path('<int:listing_id>', views.listing, name='listing'),
    # /listings/search sayfamız için
    path('search', views.search, name='search'),
]