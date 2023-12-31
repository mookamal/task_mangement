from django.urls import path
from .views import BoardsListView , create_board , BoardDetail , create_list , create_card , change_desc_in_card
urlpatterns = [
    path("",BoardsListView.as_view(),name="board_list"),
    path("<int:pk>",BoardDetail.as_view(),name="board_detail"),
    path("create_board",create_board,name="create_board"),
    path("create_list",create_list,name="create_list"),
    path("create_card",create_card,name="create_card"),
    path("change_desc_in_card",change_desc_in_card,name="change_desc_in_card"),
]
