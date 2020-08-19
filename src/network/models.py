from django.db import models

class Station(models.Model):
    station_name    = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.station_name

class Line(models.Model):
    line_color      = models.CharField(max_length=50, blank=False)
    line_color_code = models.CharField(max_length=10, blank=False)
    line_fare       = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    average_speed   = models.PositiveIntegerField()

    def __str__(self):
        return self.line_color

class Track(models.Model):
    source          = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='tracks_to', blank=False)
    destination     = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='tracks_from', blank=False)
    track_line      = models.ForeignKey('Line', on_delete=models.CASCADE, blank=False)
    distance        = models.PositiveIntegerField()
