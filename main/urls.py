from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('employee/<str:name>/',demo, name='demo'),
    path('create-products/', create_products, name='create_products'),
    path('products/<str:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path("json/",show_json, name="show_json"),
    path("xml/<str:id>/",show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>/",show_json_by_id, name="show_json_by_id"),
    path('add-employee',create_employee, name="add_employee")
]