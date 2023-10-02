from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from board.models import Card
from .models import CheckList
from django.core.serializers import serialize
# Create your views here.

@login_required
def add_checklist(request):
    if request.method == "POST":
        id_card = request.POST.get("id-card")
        title_checklist = request.POST.get("title-checklist")
        get_card = Card.objects.get(id=id_card)
        if get_card:
            checkList = CheckList.objects.create(
                title=title_checklist,
                card=get_card
            )
            checkList.save()
            checkList = serialize('json',[checkList])
            return JsonResponse({"success":f"Checklist added successfully for this card!","checkList":checkList,})

    return JsonResponse({"error":"Invalid request"})

@login_required
def get_items(request):
    if request.method == "GET":
        checklist_id = request.GET.get("checklist-id")
        print(checklist_id)
        return JsonResponse({"success":"success"})


    return JsonResponse({"error":"Invalid request"})