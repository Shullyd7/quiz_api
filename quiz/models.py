from django.db import models

# Create your models here.



class Question(models.Model):
    text = models.CharField(max_length=255)
    options = models.JSONField(blank=True, null=True)
    correct_option = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question, related_name='quizzes')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    answers = models.JSONField()
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s response to {self.quiz}"