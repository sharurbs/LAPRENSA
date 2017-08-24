from django.db import models

# Create your models here.
class cualquiera (models.Model):

Title=models.CharField(max_length=50,help_text='Escriba su nombre')
number=models.AutoField(max_lenght=10,help_text='Escriba su telefono')
genere=models.CharField(max_lenght=1,help_text='Ingrese su genero')
pday=models.DateField(help_text='Ingrese su fecha de nacimiento')
