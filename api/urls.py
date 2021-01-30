from django.conf.urls import url
from .views import RoomView

urlpatterns = [
    url('', RoomView.as_view())
]
