from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.january),
    # path("february",views.february)

    path("<int:month>",views.monthly_challenge_by_number),  # if the entered url endpoint is number this function will be called
    path("<str:month>", views.monthly_challenge)
]