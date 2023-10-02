from django.urls import path
from .views import add_checklist 
urlpatterns = [
    path("add_checklist/",add_checklist,name="add_checklist"),


]
