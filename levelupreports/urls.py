from django.urls import path
from .views import (usergame_list, user_event_list)

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', user_event_list),
]
