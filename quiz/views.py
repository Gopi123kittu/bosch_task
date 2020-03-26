from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question, Quiz
import json
from django.views import generic

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        print("suer data", request["POST"])

def get_quiz_list(request):
    quiz_list = []
    for quiz_data in Quiz.objects.all():
        quiz_list.append(quiz_data)
    data = {'quiz_data': quiz_list}
    #return HttpResponse(json.dumps({"data": quiz_list}, indent=4))
    return render(request, 'quizlist.html',data)

# def show_quiz(request, quiz_id):
   # que = Question.objects.filter(quiz_detail=1)



    

    
    
