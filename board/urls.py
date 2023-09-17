from django.urls import path
from .views import BoardsListView , create_board
urlpatterns = [
    path("",BoardsListView.as_view(),name="board_list"),
    path("create_board",create_board,name="create_board"),
    
]
