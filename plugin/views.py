from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from board.models import Card
from .models import CheckList , ItemCheckList
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
def add_item_to_checklist(request):
    if request.method == "POST":
        checklist_id = request.POST.get("id-checklist")
        item_checklist_name = request.POST.get("item-checklist-name")
        get_checkList = CheckList.objects.get(id=checklist_id)
        if get_checkList:
            item_checkList = ItemCheckList.objects.create(
                name=item_checklist_name,
                checklist= get_checkList,
            )
            item_checkList.save()
            to_json = serialize('json' , [item_checkList])
            return JsonResponse({"success":"success","item":to_json})


    return JsonResponse({"error":"Invalid request"})

@login_required
def change_status_item_checklist(request):
    if request.method == "POST":
        id_item = request.POST.get("id-item")
        get_item = ItemCheckList.objects.get(id=id_item)
        if get_item:
            get_item.status = not get_item.status
            get_item.save()
            return JsonResponse({"success":"success"})
    return JsonResponse({"error":"Invalid request"})