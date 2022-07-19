from django.db import models

class Curso(models.Model):
    
    curso_titulo = models.CharField(max_length=255)
    curso_contenido = models.TextField()
    curso_publicado = models.DateTimeField("Fecha de Publicación")
    
    def __str__(self):
        return self.curso_titulo
