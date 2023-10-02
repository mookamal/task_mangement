from django.db import models
from board.models import Card
# Create your models here.

class CheckList(models.Model):
    title = models.CharField(max_length=50)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return str(f"{self.title} : to card : {self.card.name}")

class ItemCheckList(models.Model):
    status = models.BooleanField(default=False)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)