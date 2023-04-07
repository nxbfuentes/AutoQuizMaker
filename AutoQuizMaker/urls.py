"""AutoQuizMaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AutoQuizMakerApp import views

app_name = 'AutoQuizMakerApp'

urlpatterns = [
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/create/', views.QuizCreateView.as_view(), name='quiz_create'),
    path('quiz/<int:pk>/update/', views.QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('quiz/<int:pk>/question/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/update/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('quiz/<int:pk>/question/<int:question_pk>/choice/create/', views.ChoiceCreateView.as_view(), name='choice_create'),
    path('question/<int:pk>/choice/<int:choice_pk>/update/', views.ChoiceUpdateView.as_view(), name='choice_update'),
    path('question/<int:pk>/choice/<int:choice_pk>/delete/', views.ChoiceDeleteView.as_view(), name='choice_delete'),
]