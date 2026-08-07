from django.db import models


class Movies(models.Model):
    title = models.CharField(unique=True, max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    class Meta:
        db_table = 'ex02_movies'
        app_label = 'ex02'

    def __str__(self):
        return self.title
