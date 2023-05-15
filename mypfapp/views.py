from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest, HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.



class IndexView(generic.ListView):
    template_name = 'mypfapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
# #404에러 일으키기
# def detail(request,question_id):
# #      try:
# #         question=Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404('Question does not exist') 
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'mypfapp/detail.html',{'question':question})

# def results(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'mypfapp/results.html',{'question':question})

class DetailView(generic.DetailView ):
    model=Question
    template_name='mypfapp/detail.html'

class ResultsView(generic.DetailView ):
    model=Question
    template_name='mypfapp/results.html'

def vote(request,question_id):
    #return HttpResponse("you're voing on question %s." %question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'mypfapp/detail.html',{
            'qusetion':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mypfapp:results', args=(question_id,)))

class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())