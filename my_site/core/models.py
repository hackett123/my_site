from django.db import models

# Create your models here.

class Blog_Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=256, default="Project Name Here")
    github = models.CharField(max_length=256, default="https:github.com/hackett123")
    description = models.TextField(default="Project Description")
    link_to_details = models.CharField(max_length=256, default="/projects/{{name}}")