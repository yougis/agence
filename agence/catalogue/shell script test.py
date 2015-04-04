from catalogue.models import Company, Scene
from photologue.models import Gallery, Photo

	scene_list = Scene.objects.order_by('title')
	carousel = []
		 
	for scene in scene_list:
		scene_gallery = scene.photo_gallery
		if scene_gallery:
		   carouselAdd = carousel.append(scene_gallery)

	print(carousel)
