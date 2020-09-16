from django.db import models

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

class Modalidad(models.Model):
    Senderismo = 'Senderismo'
    Trekking = 'Trekking'
    Montanismo = 'Montañismo'
    Alpinismo = 'Alpinismo'
    Ciclismo = 'Ciclismo'
    MODALIDAD_CHOICES = [
        (Senderismo, 'Senderismo'),
        (Trekking, 'Trekking'),
        (Montanismo, 'Montañismo'),
        (Alpinismo, 'Alpinismo'),
        (Ciclismo, 'Ciclismo'),
    ]
    modalidad = models.CharField(max_length=15,
                                 choices=MODALIDAD_CHOICES,
                                 default=Senderismo,
                                 )

class Tematica(models.Model):
    GEOGRAFICA = 'GEO'
    BIOLOGICA = 'BIO'
    CULTURAL = 'CUL'
    GEN = 'GEN'
    EXP = 'EXP'
    TEMATICA_CHOICES = [
        (GEOGRAFICA, 'Geografica'),
        (BIOLOGICA, 'Biologica'),
        (CULTURAL, 'Cultural'),
        (GEN, 'Gen'),
        (EXP, 'Exp'),
    ]
    tematica = models.CharField(max_length=10,
                                choices=TEMATICA_CHOICES,
                                default=GEOGRAFICA,
                                )

class Medio(models.Model):
    Tierra = 'Tierra'
    Agua = 'Agua'
    Aire = 'Aire'
    MEDIO_CHOICES = [
        (Tierra, 'Tierra'),
        (Agua, 'Agua'),
        (Aire, 'Aire'),
    ]
    medio = models.CharField(max_length=10,
                             choices=MEDIO_CHOICES,
                             default=Tierra,
                             )

class Nivel(models.Model):
    Alto = 'Alto'
    Medio = 'Medio'
    Bajo = 'Bajo'
    NIVEL_CHOICES = [
        (Alto, 'Alto'),
        (Medio, 'Medio'),
        (Bajo, 'Bajo'),
    ]
    nivel = models.CharField(max_length=10,
                             choices=NIVEL_CHOICES,
                             default=Alto,
                             )

class Tipo(models.Model):
    Viaje = 'Viaje'
    Excursion = 'Excursion'
    TIPO_CHOICES = [
        (Viaje, 'Viaje'),
        (Excursion, 'Excursion'),
    ]
    tipo = models.CharField(max_length=15,
                            choices=TIPO_CHOICES,
                            default=Viaje,
                            )

class Ambito(models.Model):
    Regional = 'Regional'
    Nacional = 'Nacional'
    Comarcal = 'Comarcal'
    AMBITO_CHOICES = [
        (Regional, 'Regional'),
        (Nacional, 'Nacional'),
        (Comarcal, 'Comarcal'),
    ]
    ambito = models.CharField(max_length=10,
                              choices=AMBITO_CHOICES,
                              default=Regional,
                              )

class Geometria(models.Model):
    Circular = 'Circular'
    Lineal = 'Lineal'
    GEOMETRIA_CHOICES = [
        (Circular, 'Circular'),
        (Lineal, 'Lineal'),
    ]
    geometria = models.CharField(max_length=10,
                                 choices=GEOMETRIA_CHOICES,
                                 default=Circular,
                                 )

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
    proveedor = models.ForeignKey()
    plazas = models.IntegerField()
    geometria = models.ForeignKey()
    tipo = models.ForeignKey()
    medio = models.ForeignKey()
    modalidad = models.ForeignKey()
    ambito = models.ForeignKey()
    tematica = models.ForeignKey()
    nivel = models.ForeignKey()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(precio__gte=0), name='precio_gte_0'),
            models.CheckConstraint(check=models.Q(plazas__gte=0), name='plazas_gte_0'),
        ]

        def __str__(self):
            return self.titulo

class Guia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    dni = models.CharField(max_length=9, unique=True)
    fechaNacimiento = models.DateField(help_text="Format: <em>DD/MM/YYYY</em>.")
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=9, unique=True)
    correo = models.EmailField(unique=True, unique=True)
    password = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellidos)

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