from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    REGION = [
        ('Arusha', 'Arusha'),('Dar es Salaam', 'Dar es Salaam'),
        ('Dodoma', 'Dodoma'),('Geita', 'Geita'),
        ('Iringa', 'Iringa'),
        ('Kagera', 'Kagera'),
        ('Katavi', 'Katavi'),
        ('Kigoma', 'Kigoma'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Lindi', 'Lindi'),
        ('Manyara', 'Manyara'),
        ('Mara', 'Mara'),
        ('Mbeya', 'Mbeya'),
        ('Mjini Magharibi', 'Mjini Magharibi'),
        ('Morogoro', 'Morogoro'),
        ('Mtwara', 'Mtwara'),
        ('Mwanza', 'Mwanza'),
        ('Njombe', 'Njombe'),
        ('Pemba North', 'Pemba North'),
        ('Pemba South', 'Pemba South'),
        ('Pwani', 'Pwani'),
        ('Rukwa', 'Rukwa'),
        ('Ruvuma', 'Ruvuma'),
        ('Shinyanga', 'Shinyanga'),
        ('Simiyu', 'Simiyu'),
        ('Singida', 'Singida'),
        ('Songwe', 'Songwe'),
        ('Tabora', 'Tabora'),
        ('Tanga', 'Tanga'),
        ('Unguja North', 'Unguja North'),
        ('Unguja South', 'Unguja South'),
    ]

    parentfull_name = models.CharField(verbose_name="Parent Full name", max_length=180,blank=True,null=True)
    full_name = models.CharField(verbose_name="Child Initals", max_length=180)
    dateofbirth =models.DateField(auto_now=False, auto_now_add=False)
    facility = models.CharField(verbose_name="Facility name", max_length=180)
    region = models.CharField(verbose_name="Region", max_length=50,choices=REGION)
    doctor = models.ForeignKey(User, verbose_name="Doctor", on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.TextField(verbose_name="Address",default="123 mikocheni Dsm")
    phonenumber = models.CharField(verbose_name="Phone number", max_length=50,blank=True,null=True)
    childAG = models.IntegerField(verbose_name="Age Grouo",default=0, null=False,blank=False)
    # address = models.TextField(verbose_name="Address")

    class Meta:
        verbose_name = 'Patient Infomartion'
        verbose_name_plural = 'Patient Infomartions'

    def __str__(self):
        return self.full_name


    def get_absolute_url(self):
        """Return absolute url for Patient."""
        return ('')