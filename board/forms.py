from django.forms import ModelForm
from .models import Board

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ["bg_color","title","Visibility"]

