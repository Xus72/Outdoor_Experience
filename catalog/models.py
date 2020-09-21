from django.db import models

from django.urls import reverse

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


class Actividad(models.Model):
    """Modelo que representa las actividades"""
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=200, blank=True)
    precio = models.FloatField()
    duracion = models.DurationField()
    fechaSalida = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    fechaRecogida = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    lugar = models.CharField(max_length=20)
    puntoPartida = models.CharField(max_length=50)
    horaPartida = models.DateTimeField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE,)
    plazas = models.IntegerField()

    GEOMETRIA = (
        ('Circular', 'Circular'),
        ('Lineal', 'Lineal'),
    )

    geometria = models.CharField(max_length=15, choices=GEOMETRIA, default='Circular')

    TIPO = (
        ('Viaje', 'Viaje'),
        ('Excursion', 'Excursion'),
    )

    tipo = models.CharField(max_length=15, choices=TIPO, default='Viaje')

    MEDIO = (
        ('Tierra', 'Tierra'),
        ('Aire', 'Aire'),
        ('Agua', 'Agua'),
    )

    medio = models.CharField(max_length=10, choices=MEDIO, default='Tierra')

    MODALIDAD = (
        ('Senderismo', 'Senderismo'),
        ('Trekking', 'Trekking'),
        ('Montañismo', 'Montañismo'),
        ('Alpinismo', 'Alpinismo'),
        ('Ciclismo', 'Ciclismo'),
    )

    modalidad = models.CharField(max_length=15, choices=MODALIDAD, default='Senderismo')

    AMBITO = (
        ('Regional', 'Regional'),
        ('Comarcal', 'Comarcal'),
        ('Nacional', 'Nacional'),
    )
    ambito = models.CharField(max_length=15, choices=AMBITO, default='Regional')

    TEMATICA = (
        ('GEO', 'Geográfica'),
        ('BIO', 'Biológica'),
        ('CUL', 'Cultural'),
        ('GEN', 'GEN'),
        ('EXP', 'EXP'),
    )

    tematica = models.CharField(max_length=3, choices=TEMATICA, default='GEO')
    NIVEL = (
        ('Alto', 'Alto'),
        ('Medio', 'Medio'),
        ('Bajo', 'Bajo'),
    )
    nivel = models.CharField(max_length=10, choices=NIVEL, default='Alto')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('actividades-detalles', args=[str(self.id)])

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(precio__gte=0), name='precio_gte_0'),
            models.CheckConstraint(check=models.Q(plazas__gte=0), name='plazas_gte_0'),
        ]

class Guia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    dni = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=9, unique=True)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellidos)

    def get_absolute_url(self):
        return reverse('guias-detalles', args=[str(self.id)])

class Participante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    dni = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField()
    municipio = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    codPostal = models.IntegerField(max_length=5)
    telefono = models.IntegerField(max_length=9)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=20)
    password = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellidos)