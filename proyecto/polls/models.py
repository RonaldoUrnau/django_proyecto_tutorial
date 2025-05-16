from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin  # Necesario para usar el decorador @admin.display

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Texto de la pregunta
    pub_date = models.DateTimeField("date published")  # Fecha de publicación

    def __str__(self):
        return self.question_text

    # Este decorador mejora cómo se muestra esta función en el admin
    @admin.display(
        boolean=True,                # Muestra como un ícono de check o cruz
        ordering="pub_date",         # Permite ordenar por pub_date al hacer clic en el encabezado
        description="¿Publicada recientemente?",  # Texto que aparece como encabezado de columna
    )
    def was_published_recently(self):
        """
        Retorna True si la pregunta fue publicada en las últimas 24 horas.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Relación con la pregunta
    choice_text = models.CharField(max_length=200)  # Texto de la opción
    votes = models.IntegerField(default=0)  # Número de votos que tiene esta opción

    def __str__(self):
        return self.choice_text
