from django.db import models
import datetime
from django.utils import timezone
# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self) :
        return self.question_text
    
    def was_published_recently(self):
        now=timezone.now()
        return now  - datetime.timedelta(days=1) <=self.pub_date <=now
    #날짜가 과거에만 있을 때만 return


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#외래 키다, 연쇄삭제 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    