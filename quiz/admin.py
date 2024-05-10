from django.contrib import admin
from .models import Question, Quiz, QuizResponse

# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizResponse)
