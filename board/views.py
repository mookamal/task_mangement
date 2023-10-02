from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect , get_object_or_404
from .models import Board , BList , Card
from django.views.generic import ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BoardForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
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
    
@login_required
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
        return redirect("home")

class BoardDetail(LoginRequiredMixin,DetailView):
    login_url = "login"
    model = Board
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        board = get_object_or_404(Board,id=self.kwargs['pk'])
        if board.Visibility == "private":
            if board.owner != request.user:
                return HttpResponse("this board not found")
        return super().get(request, *args, **kwargs)
    
@login_required
def create_list(request):
    if request.method == "POST":
        board_id_value = request.POST.get('board_id')
        list_name = request.POST.get('list_name')
        board = Board.objects.get(id=board_id_value)
        if board.owner == request.user:
            BList.objects.create(
                name=list_name,
                board=board
            )
        
        return redirect('board_detail', pk=board_id_value)

@login_required
def create_card(request):
    if request.method == "POST":
        list_id = request.POST.get('list_id')
        b_list = BList.objects.get(id=list_id)
        id_board = b_list.board.id
        if b_list.board.owner == request.user:
            card_name = request.POST.get('card_name')
            Card.objects.create(
                name=card_name,
                b_list=b_list
            )

            return redirect('board_detail', pk=id_board)

@login_required
def change_desc_in_card(request):
    if request.method == 'POST':
        desc = request.POST.get("change-desc")
        id_card = request.POST.get("id-card")
        get_card = Card.objects.get(id=id_card)
        if get_card:
            get_card.desc = desc
            get_card.save()
            return JsonResponse({'success': 'Description changed successfully!'})        
    return JsonResponse({'error': 'Invalid request'})