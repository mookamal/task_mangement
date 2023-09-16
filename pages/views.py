from django.shortcuts import render , redirect
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = "home/home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("board_list")
        return super().dispatch(request, *args, **kwargs)
    