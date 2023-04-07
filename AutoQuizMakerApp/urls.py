from django.urls import path
from . import views

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
