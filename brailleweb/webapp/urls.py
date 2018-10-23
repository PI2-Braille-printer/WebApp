from . import views
from django.urls import include, path

app_name = 'webapp'
urlpatterns = [
    path('uploadfile/', views.upload_file_form, name='upload_file_form'),
    path('uploadtext/', views.text_form, name='text_form'),
    path('downloadfile/', views.download_file, name='download_file'),
    path('', views.index, name='index'),
]