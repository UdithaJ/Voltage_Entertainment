from django.urls import path
from.import views


urlpatterns = [
    path('',views.sound_admin_upload,name = 'sound_admin_upload')
]

urlpatterns = [
    path('',views.sound_main,name = 'sound_main')
]