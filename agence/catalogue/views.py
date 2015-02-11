from django.shortcuts import render
from django.http import HttpResponse


from catalogue.models import Company, Scene


def index(request):
    all_scene_by_cie = Company.objects.order_by('name')
    context = {'all_scene_by_cie': all_scene_by_cie}
    return render(request, 'catalogue/index.html', context)


def detail(request, scene_id):
    return HttpResponse("vous regardez le spectacle %s." % scene_id)