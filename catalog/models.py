from django.db import models
from django.urls import reverse
import datetime

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    personaContacto = models.CharField(max_length=20)
    cif = models.CharField(max_length=9, unique=True)
    tipoEntidad = models.CharField(max_length=20)
    direccion = models.TextField(max_length=100)
    localidad = models.CharField(max_length=20)
    telefono = models.IntegerField(max_length=9, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (("add_prov", "Añadir proveedor"),("edit_prov", "Editar proveedor"), ("rem_prov", "Eliminar proveedor"),)


class Actividad(models.Model):
    """Modelo que representa las actividades"""
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=200, blank=True)
    precio = models.FloatField()
    fechaSalida = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    fechaRecogida = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    duracion = models.CharField(max_length=10)
    lugar = models.CharField(max_length=20)
    puntoPartida = models.CharField(max_length=50)
    horaPartida = models.TimeField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE,)
    plazas = models.IntegerField()

    GEOMETRIA = (
        ('Circular', 'Circular'),
        ('Lineal', 'Lineal'),
    )

    geometria = models.CharField(max_length=15, choices=GEOMETRIA)

    TIPO = (
        ('Viaje', 'Viaje'),
        ('Excursion', 'Excursion'),
    )

    tipo = models.CharField(max_length=15, choices=TIPO)

    MEDIO = (
        ('Tierra', 'Tierra'),
        ('Aire', 'Aire'),
        ('Agua', 'Agua'),
    )

    medio = models.CharField(max_length=10, choices=MEDIO)

    MODALIDAD = (
        ('Senderismo', 'Senderismo'),
        ('Trekking', 'Trekking'),
        ('Montañismo', 'Montañismo'),
        ('Alpinismo', 'Alpinismo'),
        ('Ciclismo', 'Ciclismo'),
    )

    modalidad = models.CharField(max_length=15, choices=MODALIDAD)

    AMBITO = (
        ('Regional', 'Regional'),
        ('Comarcal', 'Comarcal'),
        ('Nacional', 'Nacional'),
    )
    ambito = models.CharField(max_length=15, choices=AMBITO)

    TEMATICA = (
        ('GEO', 'Geográfica'),
        ('BIO', 'Biológica'),
        ('CUL', 'Cultural'),
        ('GEN', 'GEN'),
        ('EXP', 'EXP'),
    )

    tematica = models.CharField(max_length=3, choices=TEMATICA)

    NIVEL = (
        ('A', 'Alto'),
        ('B', 'Medio'),
        ('C', 'Bajo'),
    )
    nivel = models.CharField(max_length=1, choices=NIVEL)
    imagen = models.ImageField(upload_to='images', blank=True)
    guia = models.ForeignKey('Guia', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('actividades-detalles', args=[str(self.id)])

    def mostrar_duracion(self):
        diferencia = self.fechaRecogida - self.fechaSalida
        return "{} dias".format(diferencia.days)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(precio__gte=0), name='precio_gte_0'),
            models.CheckConstraint(check=models.Q(plazas__gte=0), name='plazas_gte_0'),
        ]

        permissions = (("add_activ", "Añadir actividad"), ("edit_activ", "Editar actividad"), ("rem_activ", "Eliminar actividad"),)


class Guia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    dni = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")

    SEXO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    sexo = models.CharField(max_length=1, choices=SEXO)
    telefono = models.CharField(max_length=9, unique=True)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=24)
    avatar = models.ImageField(upload_to='images/avatar', blank=True, default='images/avatar/no_image.png')

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellidos)

    def get_absolute_url(self):
        return reverse('guias-detalles', args=[str(self.id)])

    class Meta:
        permissions = (("edit_guia", "Editar guia"),)

class Participante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    dni = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField()
    municipio = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    codPostal = models.IntegerField(max_length=5)

    SEXO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO)
    telefono = models.IntegerField(max_length=9)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=20)
    password = models.CharField(max_length=24)
    avatar = models.ImageField(upload_to='images/avatar', blank=True, default='images/avatar/no_image.png')

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellidos)

    def get_absolute_url(self):
        return reverse('participantes-detalles', args=[str(self.id)])
