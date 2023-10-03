from django.urls import path
from .views import add_checklist ,add_item_to_checklist , change_status_item_checklist
urlpatterns = [
    path("add_checklist/",add_checklist,name="add_checklist"),
    path("add_item_to_checklist/",add_item_to_checklist,name="add_item_to_checklist"),
    path("change_status_item_checklist/",change_status_item_checklist,name="change_status_item_checklist"),
    
]
