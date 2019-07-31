from django.db import models


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    terrain = models.CharField(max_length=255, blank=True)
    elevation = models.IntegerField(default=0)
    coordinates = models.CharField(max_length=32, default="()")
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    n_to = models.IntegerField(blank=True, null=True)
    s_to = models.IntegerField(blank=True, null=True)
    e_to = models.IntegerField(blank=True, null=True)
    w_to = models.IntegerField(blank=True, null=True)

    def connectRooms(self, direction, previousRoom, currentRoom):
        if direction == "n":
            self.s_to = previousRoom
            pr = Room.objects.get(id=previousRoom)
            pr.n_to = currentRoom
            pr.save()
        elif direction == "s":
            self.n_to = previousRoom
            pr = Room.objects.get(id=previousRoom)
            pr.s_to = currentRoom
            pr.save()
        elif direction == "e":
            self.w_to = previousRoom
            pr = Room.objects.get(id=previousRoom)
            pr.e_to = currentRoom
            pr.save()
        elif direction == "w":
            self.e_to = previousRoom
            pr = Room.objects.get(id=previousRoom)
            pr.w_to = currentRoom
            pr.save()
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def __str__(self):
        return f"Room {self.id}"


class Player(models.Model):
    name = models.CharField(max_length=255, editable=True)
    current_room = models.IntegerField(default=0)
    cooldown = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=False)
    encumbrance = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    def __str__(self):
        return self.name
