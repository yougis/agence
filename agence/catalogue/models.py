from django.db import models
from photologue.models import Gallery, Photo

class SceneCat(models.Model):
    category = models.CharField(max_length=200)

    def __unicode__(self):
	return self.category


class Age(models.Model):
    category = models.CharField(max_length=200)

    def __unicode__(self):
	return self.category

class Duration(models.Model):
    hour = models.IntegerField(blank=True, null=True)
    minute = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=200, blank=True, null=True)    

    def __unicode__(self):
	return self.condition

class Partnership(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ForeignKey(Photo, blank=True, null=True)
    
    def __unicode__(self):
	return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    resume = models.CharField(blank=True, max_length=2000, null=True)
    workshop_price = models.IntegerField(blank=True, null=True)
    workshop_term = models.CharField(blank=True, max_length=200, null=True)
    logo = models.ForeignKey(Photo, blank=True, null=True)
    photo_gallery = models.ForeignKey(Gallery, blank=True, null=True)

    def __unicode__(self):
           return self.name


class Scene(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200, null=True)
    scene_cat =  models.ManyToManyField(SceneCat, blank=True, null=True)
    synops = models.CharField(blank=True, max_length=2000, null=True)
    interpret = models.CharField(blank=True, max_length=500, null=True)
    age = models.ForeignKey(Age, blank=True, null=True)
    duration = models.ForeignKey(Duration, blank=True, null=True)
    full_price = models.IntegerField(blank=True, null=True)
    full_nb_people = models.IntegerField(blank=True, null=True)
    light_price = models.IntegerField(blank=True, null=True)
    light_nb_people = models.IntegerField(blank=True, null=True)
    teazer_url = models.CharField(blank=True, max_length=200, null=True)
    disponibility = models.CharField(blank=True, max_length=200, null=True)
    photo_gallery = models.ForeignKey(Gallery, blank=True, null=True)    
    dossier_presse = models.FileField(upload_to="dossiers_presse/", null=True, blank=True)
    dossier_peda = models.FileField(upload_to="dossiers_peda/", null=True, blank=True)
    archive_zip = models.FileField(upload_to="archives_zip/", null=True, blank=True)
 
    def __unicode__(self):             
        return self.title
