from django.urls import path
from .views import RegisterView, RetrieveUserView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view())
]
