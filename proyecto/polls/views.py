from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import Question, Choice
from django.utils import timezone

# Vista genérica para mostrar la lista de preguntas
class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Retorna las últimas 5 preguntas publicadas (excluyendo las del futuro).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# Vista genérica para mostrar los detalles de una pregunta
class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"

    def get_queryset(self):
        """
        Excluye cualquier pregunta que aún no haya sido publicada.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# Vista genérica para mostrar los resultados de una pregunta
class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"

# Voto para una pregunta, sin vista genérica
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

