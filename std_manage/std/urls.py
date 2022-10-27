from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/",home),
    path("add-std/",std_add),
    path("delete-std/<int:card>",delete_std),
    path("update-std/<int:card>",update_std),
    path("do-update-std/<int:card>",do_update_std),
]