from django.db import models

# Create your models here.
class Recordings(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='recordings/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title