from django.urls import path
from .views import QuestionListCreate, QuestionRetrieveUpdateDestroy, QuizListCreate, QuizRetrieveUpdateDestroy, SubmitQuiz

urlpatterns = [
    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroy.as_view(), name='question-retrieve-update-destroy'),
    path('quizzes/', QuizListCreate.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroy.as_view(), name='quiz-retrieve-update-destroy'),
    path('quizzes/<int:quiz_id>/submit/', SubmitQuiz.as_view(), name='submit_quiz'),
]