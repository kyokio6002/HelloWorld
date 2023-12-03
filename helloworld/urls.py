from django.urls import path

from .views import HelloWord

app_name = 'helloworld'

urlpatterns = [
    path('', HelloWord.as_view(), name='helloworld'),
]
