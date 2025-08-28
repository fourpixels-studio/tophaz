from django.urls import path
from .views import index, bio, bookings


urlpatterns = [
    path("", index, name="index"),
    path("bio/", bio, name="bio"),
    path("bookings/", bookings, name="bookings"),
]
