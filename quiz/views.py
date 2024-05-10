from django.shortcuts import render
from rest_framework import generics
from .models import Question, Quiz, QuizResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import QuestionSerializer, QuizSerializer, ResponseSerializer
# Create your views here.




class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class SubmitQuiz(APIView):
    def post(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        user = request.data.get('user')
        answers = request.data.get('answers')

        # Validate if answers are provided
        if not answers:
            return Response({"answers": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        # Quiz ID is provided in the URL path, no need to include it in the response data
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get IDs of all questions in the quiz
        question_ids = set(str(question.id) for question in quiz.questions.all())

        # Check if answers contain every and exact question IDs in the related quiz ID
        if not set(answers.keys()) == question_ids:
            return Response({"error": "Answers should contain every and exact question IDs in the related quiz ID"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Calculate score
        score = 0

        # Iterate through each question ID in the provided answers
        for question_id, answer in answers.items():
            # Get the corresponding question object
            question = Question.objects.get(pk=int(question_id))
            # If the answer provided by the user matches the correct option, increment the score
            if answer == question.correct_option:
                score += 1

        # Create response data
        response_data = {
            "user": user,
            "score": score,
            "total_questions": quiz.questions.count(),
            "quiz": quiz_id,  # Assign quiz ID to the quiz field
            "answers": answers  # Assign answers to the answers field
        }

        # Serialize response data
        serializer = ResponseSerializer(data=response_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)