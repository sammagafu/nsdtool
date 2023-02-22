from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(verbose_name="Full name", max_length=180)
    dateofbirth =models.DateField(auto_now=False, auto_now_add=False)
    facility = models.CharField(verbose_name="Facility name", max_length=180)
    height = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        verbose_name = 'Patient Infomartion'
        verbose_name_plural = 'Patient Infomartions'

    def __str__(self):
        return self.full_name


    def get_absolute_url(self):
        """Return absolute url for Patient."""
        return ('')