from django.db import models

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name
