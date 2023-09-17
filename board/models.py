from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
# Create your models here.

class Board(models.Model):
    VISIBILITY = [("private","private"),("public","public")]
    title = models.CharField(max_length=100)
    Visibility = models.CharField(max_length=20,choices=VISIBILITY)
    bg_color = ColorField(default='#fff')
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ManyToManyField(User,blank=True ,related_name="team_board")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)

class BList(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"list name {str(self.name)} from board {str(self.board.title)}"

class Card(models.Model):
    name = models.CharField(max_length=100)
    b_list = models.ForeignKey(BList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"card : {str(self.name)} to list name {str(self.b_list.name)}"