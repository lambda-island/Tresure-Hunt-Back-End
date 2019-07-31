from django.db import models


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    terrain = models.CharField(max_length=255, blank=True)
    elevation = models.IntegerField(default=0)
    x = models.IntegerField()
    y = models.IntegerField()
    n_to = models.IntegerField(blank=True, null=True)
    s_to = models.IntegerField(blank=True, null=True)
    e_to = models.IntegerField(blank=True, null=True)
    w_to = models.IntegerField(blank=True, null=True)
    
