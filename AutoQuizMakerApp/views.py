from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Quiz, Question, Choice

# Quiz views

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'

class QuizCreateView(CreateView):
    model = Quiz
    fields = ['title', 'description']
    template_name = 'quiz_form.html'
    success_url = reverse_lazy('quiz_list')

class QuizUpdateView(UpdateView):
    model = Quiz
    fields = ['title', 'description']
    template_name = 'quiz_form.html'
    success_url = reverse_lazy('quiz_list')

class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz_confirm_delete.html'
    success_url = reverse_lazy('quiz_list')

# Question views

class QuestionCreateView(CreateView):
    model = Question
    fields = ['quiz', 'text']
    template_name = 'question_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.quiz.pk})

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['quiz', 'text']
    template_name = 'question_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.quiz.pk})

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'question_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.quiz.pk})

# Choice views

class ChoiceCreateView(CreateView):
    model = Choice
    fields = ['question', 'text', 'is_correct']
    template_name = 'choice_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.question.quiz.pk})

class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ['question', 'text', 'is_correct']
    template_name = 'choice_form.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.question.quiz.pk})

class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('quiz_detail', kwargs={'pk': self.object.question.quiz.pk})
