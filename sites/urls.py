from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('sites/<str:site_name>', views.page, name='page'),
]