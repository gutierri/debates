from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import Group

class Room(models.Model):
    room_name = models.CharField(max_length=42)
    room_slug = models.CharField(max_length=84, editable=False)
    groups_permissions = models.ManyToManyField(Group, blank=True)

    def save(self):
            if not self.id:
                self.room_slug = slugify(self.room_name)
            super(Room, self).save()

    def __str__(self):
        return self.room_name
