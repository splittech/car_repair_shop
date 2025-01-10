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
         'orders/create',
         views.order_list,
         name='create_order'
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
     # path(
     #     'profile_edit/<slug:username>/',
     #     views.UpdateUser.as_view(),
     # #     views.profile,
     #     name='edit_profile'
     # ),
     path(
        'profile/<int:pk>/edit/',
        views.UpdateUser.as_view(),
        name='edit_profile'
     ),
     path(
         'profile/<slug:username>/',
         views.profile,
         name='profile'
     ),
     
]
