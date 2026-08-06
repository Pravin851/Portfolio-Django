from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


class experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    certificate = models.FileField(upload_to="certificates/")
    image = models.ImageField(upload_to="images/", null=True)


class resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")
    image = models.ImageField(upload_to="images/", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)
