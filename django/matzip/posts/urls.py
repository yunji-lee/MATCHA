from django.urls import path, include
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='index'),

    path('main/', views.main, name='main'),
    path('lists/', views.lists, name='lists'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('personal_info/', views.personal_info, name='personal_info'),
    path('start_check_list/', views.start_check_list, name='start_check_list'),
    path('star_rating/<int:post_id>', views.star_rating, name="star_rating"),
]
