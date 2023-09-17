from django.shortcuts import render , redirect
from .models import Board
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BoardForm
# Create your views here.

class BoardsListView(LoginRequiredMixin,ListView):
    model = Board
    login_url = "login"
    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BoardForm()
        return context
    
    
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
        return redirect("home")