from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # Usamos la vista genérica ListView para mostrar la lista de preguntas
    path("", views.IndexView.as_view(), name="index"),
    
    # Usamos la vista genérica DetailView para mostrar los detalles de una pregunta
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # Usamos la vista genérica DetailView para mostrar los resultados de una pregunta
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Vista de votación, que sigue siendo una vista personalizada
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
