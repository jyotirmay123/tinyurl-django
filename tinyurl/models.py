from django.db import models

class Urls(models.Model):
    full_url = models.CharField(max_length=300, unique=True)
    tiny_url = models.CharField(max_length=50)
    quoted_tiny_url = models.CharField(max_length=100)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s %d" % (self.full_url, self.tiny_url, self.quoted_tiny_url, self.hits)

