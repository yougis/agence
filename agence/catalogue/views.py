from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django_tables2   import RequestConfig
from catalogue.models import Company, Scene, SceneTableFull, SceneTableLight
from photologue.models import Gallery, Photo



@login_required
def pro(request):
	 scene_table = SceneTableFull(Scene.objects.order_by('title'))
	 RequestConfig(request, paginate=False).configure(scene_table)
	 pro = True
	 return render(request, 'catalogue/pro.html', {'scene_table': scene_table, 'pro':pro})

@login_required
def proLight(request):
	 scene_table = SceneTableLight(Scene.objects.order_by('title'))
	 RequestConfig(request, paginate=False).configure(scene_table)
	 pro = False
	 return render(request, 'catalogue/pro.html', {'scene_table': scene_table, 'pro':pro})

def newsletter(request):
	return render(request, 'catalogue/newsletter.html')

def index(request):
	company_list = Company.objects.order_by('name')
	scene_list = Scene.objects.order_by('title')
	cover = Photo.objects.filter(title='cover')
	scene_photo_list = []
	for scene in scene_list:
		if scene.photo_gallery:
			if scene.photo_gallery.photos:
				scene_photo_list.append(scene)
	return render(request, 'catalogue/index.html', {'company_list':  company_list, 'scene_list': scene_list, 'scene_photo_list':scene_photo_list, 'cover': cover})

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
