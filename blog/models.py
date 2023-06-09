from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


