from django.db import models


class Davlat(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Club(models.Model):
    nom = models.CharField(max_length=30)
    logo = models.FileField(blank=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    president = models.CharField(max_length=30, blank=True)
    coach = models.CharField(max_length=30, blank=True)
    yili = models.DateField(blank=True)
    record_transfer = models.CharField(max_length=30, blank=True)
    record_sotuv = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nom


class Player(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)
    tugulgan_sana = models.DateField()
    narx = models.PositiveSmallIntegerField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    pozitsiya = models.CharField(max_length=30)

    def __str__(self):
        return self.ism


class HMavsum(models.Model):
    hozirgi_mavsum = models.CharField(max_length=10)

    def __str__(self):
        return self.hozirgi_mavsum

    class Meta:
        verbose_name = "Hozirgi Mavsum"
        verbose_name_plural = "Hozirgi Mavsum"


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    eski_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="sotuvlari")
    yangi_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="olganlari")
    narx = models.PositiveSmallIntegerField()
    tah_narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        m = HMavsum.objects.last().hozirgi_mavsum
        if self.mavsum == m:
            player = self.player
            player.club = self.yangi_club
            player.save()
        super(Transfer, self).save(*args, **kwargs)

    def __str__(self):
        return self.player.ism
