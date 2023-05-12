from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest, HttpResponse,Http404
from django.template import loader
from .models import Question
# Create your views here.


def index(request ):
    lastest_question_list=Question.objects.order_by('-pub_date')[:5] #날짜순으로 
    #output=', '.join([q.question_text for q in lastest_question_list]) #콤마로 연결하겠다.
    #template=loader.get_template('mypfapp/index.html') 
    context={
        'lastest_question_list':lastest_question_list
    }#연결해준다. 
    return render(request,'mypfapp/index.html',context)

#404에러 일으키기
def detail(request,question_id):
#      try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist') 
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'mypfapp/detail.html',{'question':question})

def results(request,question_id):
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("you're voing on question %s." %question_id)