from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Question(models.Model):
    quiz_detail = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text





