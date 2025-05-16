from django.contrib import admin
from .models import Question, Choice

# Muestra las opciones (Choices) embebidas dentro del formulario de cada pregunta (Question)
class ChoiceInline(admin.TabularInline):  # TabularInline muestra las opciones en una tabla
    model = Choice
    extra = 3  # Muestra 3 campos vacíos para agregar opciones nuevas

# Personaliza cómo se administra el modelo Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),  # Campo de texto principal de la pregunta
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),  # Campo de fecha, colapsable
    ]
    inlines = [ChoiceInline]  # Muestra las opciones directamente al editar una pregunta
    list_display = ["question_text", "pub_date", "was_published_recently"]  # Columnas que se ven en la lista
    list_filter = ["pub_date"]  # Agrega un filtro por fecha al costado derecho del admin
    search_fields = ["question_text"]

# Registra el modelo Question con la configuración personalizada
admin.site.register(Question, QuestionAdmin)

# Ahora también registramos Choice por separado para que tenga su propia interfaz
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')
    search_fields = ('choice_text',)

admin.site.register(Choice, ChoiceAdmin)
