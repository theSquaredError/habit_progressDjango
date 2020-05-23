from django.urls import path

from . import views

urlpatterns = [
    path('', views.habit, name='habit_app'),
    # path('habits', views.HabitList.as_view(), name='habits'),
    path('create', views.habit_create_view, name='create'),
    path('<int:habit_id>', views.detail, name="detail"),
]