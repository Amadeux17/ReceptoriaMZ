from django.db import models

# Create your models here.


class rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        db_table: "rol"


class personas(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rolid = models.ForeignKey(rol, null=False,
                              blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}".format(self.nombre + self.apellido)

    class Meta:
        db_name: "personas"
