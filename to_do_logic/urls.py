from to_do_logic.views import ToDoListAPIView, ToDoDetailAPIView
from django.urls import path
from to_do_logic import views


urlpatterns = [
    #url for ToDoListAPIView (create to do list and show to do list)
    path('class_api_view/ToDo/', views.ToDoListAPIView.as_view()),
    #url for ToDoDetailAPIView (show to do list, update to do list, delete to do list, complete to do list)
    path('class_api_view/ToDo/<int:pk>/', views.ToDoDetailAPIView.as_view()),
]