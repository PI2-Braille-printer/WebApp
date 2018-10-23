from . import views
from django.urls import include, path

app_name = 'webapp'
urlpatterns = [
    path('upload/', views.upload_file_form, name='upload_form'),
]