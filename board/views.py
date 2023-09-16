from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Board
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BoardsListView(LoginRequiredMixin,ListView):
    model = Board
    template_name = "board/board_list.html"
    login_url = "login"
    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)