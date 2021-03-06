# -*- coding: utf-8 -*-
from django.db import models
import django_tables2 as tables
from photologue.models import Gallery, Photo

class SceneCat(models.Model):
    category = models.CharField(max_length=200)

    def __unicode__(self):
	return self.category


class Age(models.Model):
    category = models.CharField(max_length=200, verbose_name="Age")

    def __unicode__(self):
	   return self.category

class Duration(models.Model):
    hour = models.IntegerField(blank=True, null=True)
    minute = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=200, blank=True, null=True)    

    def __unicode__(self):
    	hour = str(self.hour)
    	minute = str(self.minute)
    	if self.hour != None:
            hour = str(self.hour)
            if self.hour > 1 and self.hour != 0:
                descH = "heures"
            else:
                descH = "heure"
        else:
            hour = ""
            descH = ""
        if self.minute  != None:
            minute = str(self.minute)
            if self.minute > 1 and self.minute != 0:
                descM = "minutes"
            else:
                descM = "minute"
        else:
            minute = ""
            descM = ""
        if self.condition == None and self.hour == None and self.minute == None :
            duration = ""
        else:
            duration = " ".join([hour,descH, minute,descM, self.condition])
        return duration

class Partnership(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ForeignKey(Photo, blank=True, null=True)
    url = models.URLField(blank=True, max_length=200, null=True)
    
    def __unicode__(self):
	   return self.name

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Compagnie")
    resume = models.TextField(blank=True, null=True)
    workshop_descr = models.TextField(blank=True, null=True)
    workshop_price = models.IntegerField(blank=True, null=True)
    workshop_term = models.CharField(blank=True, max_length=200, null=True)
    logo = models.ForeignKey(Photo, blank=True, null=True)
    photo_gallery = models.ForeignKey(Gallery, blank=True, null=True)

    def __unicode__(self):
    	return self.name
  
class Scene(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200, null=True, verbose_name="Spectacle")
    scene_cat =  models.ManyToManyField(SceneCat, blank=True, null=True)
    synops = models.TextField(blank=True, null=True)
    interpret = models.CharField(blank=True, max_length=500, null=True)
    age = models.ForeignKey(Age, blank=True, null=True)
    duration = models.ForeignKey(Duration, blank=True, null=True, verbose_name="Durée")
    full_price = models.IntegerField(blank=True, null=True, verbose_name="Prix max")
    full_nb_people = models.IntegerField(blank=True, null=True, verbose_name="Nb comedien max")
    light_price = models.IntegerField(blank=True, null=True, verbose_name="Prix min")
    light_nb_people = models.IntegerField(blank=True, null=True, verbose_name="Nb comedien min")
    teazer_url = models.URLField(blank=True, max_length=200, null=True, verbose_name="Teazer")
    disponibility = models.CharField(blank=True, max_length=200, null=True, verbose_name="Disponibilité")
    photo_gallery = models.ForeignKey(Gallery, blank=True, null=True)    
    dossier_presse = models.FileField(upload_to="dossiers_presse/", null=True, blank=True, verbose_name="Dossier Presse")
    dossier_peda = models.FileField(upload_to="dossiers_peda/", null=True, blank=True, verbose_name="Dossier Pédagogique")
    archive_zip = models.FileField(upload_to="archives_zip/", null=True, blank=True, verbose_name="Archive")
    technic_file = models.FileField(upload_to="fiche_tech/", null=True, blank=True, verbose_name="Fiche technique")
    full_jauge = models.IntegerField(blank=True, null=True, verbose_name="Jauge")
    plateau_min_size = models.IntegerField(blank=True, null=True, verbose_name="Plateau")
    representation_site = models.TextField(blank=True, null=True, verbose_name="Lieu de représentation")
    electric_need = models.CharField(blank=True, max_length=200, null=True, verbose_name="Electricité")
 
    def __unicode__(self):             
        return self.title
  
class SceneTableFull(tables.Table):
    company = tables.Column(accessor='company.name')
    title = tables.Column()
    age = tables.Column(accessor='age.category')
    full_price = tables.Column(verbose_name="Prix")
    full_nb_people = tables.Column(verbose_name="Nb comedien")
     
    class Meta:
        model = Scene
        exclude = ("id","synops", "interpret", "photo_gallery", "light_price", "light_nb_people")
        attrs = {"class": "paleblue"}
        
class SceneTableLight(tables.Table):
    company = tables.Column(accessor='company.name')
    title = tables.Column()
    age = tables.Column(accessor='age.category')
    light_price = tables.Column(verbose_name="Prix")
    light_nb_people = tables.Column(verbose_name="Nb comedien")
     
    class Meta:
        model = Scene
        exclude = ("id","synops", "interpret", "photo_gallery","full_price", "full_nb_people")
        attrs = {"class": "paleblue"}

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
