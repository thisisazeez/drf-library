from django.db import models



class Books(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title