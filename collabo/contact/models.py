from django.db import models

#table creation
class details(models.Model):
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username +'-'+ self.message +'-'+ self.email