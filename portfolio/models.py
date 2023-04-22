from django.db import models

# Create your models here. A model is tippicaly a class of an database table witch
# have rows and every row has properties
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    blogImage = models.ImageField(upload_to='portfolio/blogImages/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title