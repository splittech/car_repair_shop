from django.urls import path  # type: ignore[import-untyped]
from . import views

app_name = 'service'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'services/<slug:service_slug>/',
        views.service_detail,
        name='service_detail'
    ),
    path(
        'orders/',
        views.order_list,
        name='order_list'
    ),
    path(
        'orders/create/<slug:service_slug>',
        views.create_order,
        name='create_order'
    ),
    path(
        'get_time_slots/',
        views.get_time_slots,
        name='get_time_slots'
    ),
    path(
        'orders/<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),
    path(
        'category/<slug:master_slug>/',
        views.master_detail,
        name='master_detail'
    ),
]
