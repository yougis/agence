from django.shortcuts import get_object_or_404, render
from catalogue.models import Company, Scene
from photologue.models import Gallery, Photo

def home(request):
	 return render(request, 'catalogue/home.html',)


def index(request):		   
    
    company_list = Company.objects.order_by('name')
    scene_list = Scene.objects.order_by('title')
    cover = Photo.objects.filter(title='cover')
    
    return render(request, 'catalogue/index.html', {'company_list':  company_list, 'scene_list': scene_list, 'cover': cover})

def detail_company(request, company_id):

    company = get_object_or_404(Company,pk=company_id)
    scene_list = company.scene_set.all()
    cover = Photo.objects.filter(title='cover_'+company.name)
    try:
       gallery = Gallery.objects.get(pk=company.photo_gallery_id)
    except Gallery.DoesNotExist:
       gallery = None
    return render(request, 'catalogue/detail.html', {'company': company, 'gallery': gallery, 'scene_list': scene_list, 'cover': cover})

def detail_scene(request, scene_id):
    scene = get_object_or_404(Scene, pk=scene_id)
    cover = Photo.objects.filter(title='cover_'+scene.title)
    try:
       gallery = Gallery.objects.get(pk=scene.photo_gallery_id)
    except Gallery.DoesNotExist:
       gallery = None
   
    return render(request, 'scene/detail.html', {'scene':scene, 'gallery': gallery, 'cover': cover})
