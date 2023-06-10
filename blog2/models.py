from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    dat_e = models.DateField()

    def __str__(self):
        return self.title
