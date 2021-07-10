from django.urls import path

from orders.views import OrderList, OrderCreate, OrderUpdate, OrderDelete, OrderRead, forming_complete, get_product_price

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<pk>/', OrderDelete.as_view(), name='delete'),
    path('read/<pk>/', OrderRead.as_view(), name='read'),
    path('forming/complete/<pk>/', forming_complete, name='forming_complete'),

    path('product/<pk>/price/', get_product_price, )
]
