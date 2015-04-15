from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from catalogue.models import Company, Scene, SceneCat, Age, Duration, Partnership


class SceneResource(resources.ModelResource):

    class Meta:
        model = Scene

class SceneAdmin(ImportExportModelAdmin):
    resource_class = SceneResource
    list_display = ('title','company')
    fieldsets = [
        (None, {'fields': [
        	'title',
        	'company',
        	'scene_cat',
        	'synops',
        	'interpret',
        	'age',
        	'duration',
       	]}),
        ('Media', {'fields': [
        	'photo_gallery',
        	'teazer_url',
        	'dossier_presse',
        	'dossier_peda',
        	'archive_zip',
        	]}),        
        ('Espace Pro',
        	{'fields': 
	        	[
	        	'technic_file',
	        	'full_price',
	        	'light_price',
	        	'full_nb_people',
	        	'light_nb_people',
	        	'disponibility',
	        	'full_jauge',
	        	'plateau_min_size',
	        	'representation_site',
	        	'electric_need',
	        	],
        	'classes': ['wide', 'extrapretty']
        	}),
    ]



class CompanyResource(resources.ModelResource):

    class Meta:
        model = Company
        
        
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(SceneCat)
admin.site.register(Age)
admin.site.register(Duration)
admin.site.register(Partnership)
