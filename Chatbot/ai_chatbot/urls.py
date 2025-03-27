from django.urls import path
from .views import chatbot_view, book_appointment_view, user_details_view

urlpatterns = [
    path("chat/", chatbot_view, name="chat"),
    path("book_appointment/", book_appointment_view, name="book_appointment"),
    path("user_details/", user_details_view, name="user_details"),
]
