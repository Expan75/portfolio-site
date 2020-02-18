from django.db import models

# Create your models here.


class Tag(models.Model):
    """ Tag model that will be used for intelligent sorting / recommendation """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Category model that will be used for intelligent sorting / recommendation """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Project Model used to showcase a Project """

    # The Basics
    name        = models.CharField(max_length=100)
    summary     = models.TextField(blank=True)
    description = models.TextField(blank=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags        = models.ManyToManyField(Tag)

    # Resources
    cover_photo      = models.FileField(upload_to='static/uploads/', blank=True) 
    thumbnail        = models.FileField(upload_to='static/uploads/', blank=True) 
    github_repo_link = models.CharField(max_length=200, blank=True)
    deployment_link  = models.CharField(max_length=200, blank=True)
    further_reading  = models.CharField(max_length=200, blank=True)
    tutorial_reading = models.CharField(max_length=200, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    ###### --- Methods Below, Attributes above ----- ######

    #  TODO: Handle upload of minified cover_photo as thumbnail /w dedicated method

    def __str__(self):
        return self.name



