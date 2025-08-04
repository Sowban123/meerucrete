from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_us'),
    path('about/', views.about_view, name='about'),
    path('product-catalogue/', views.product_catalogue_view, name='product_catalogue'),
    path('products/', views.product_section, name='product_section'),  # Note the URL '/products/' here
    path('submit-enquiry/', views.save_enquiry, name='save_enquiry'),  # This should be here too
]

