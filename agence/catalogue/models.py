from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):             
        return self.name

class Scene(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200)

    def __unicode__(self):             
        return self.title
