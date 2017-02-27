# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from question.models import question, answer
#from question.models import answer
from question.forms import QuestionForm

#索引頁面：所有既有資料呈現
#def questions(request):
#        questions = question.objects.all()
#        response_string = "Questions <br/>"
#        response_string += '<br/>'.join(["id: %s, subject: %s" % (q.id, q.subject) for q in questions])
#        return HttpResponse(response_string)
      
def questions(request):
        questions = question.objects.all()
        return render_to_response('questions.html',{'questions': questions})

def answers(request):
        answers = answer.objects.all()
        response_string = "answers <br/>"
        response_string += '<br/>'.join(["id: %s, content: %s" % (a.id, a.content) for a in answers])
        return HttpResponse(response_string)

#個別項目：個別既有資料呈現
#def question_detail(request, question_id):
#        question_individual = question.objects.get(pk=question_id)
#        return HttpResponse("%s" % question_individual.subject)
    
def question_detail(request, question_id):
        question_individual = question.objects.get(pk=question_id)
        return render_to_response('question_detail.html',{'question': question_individual})
    
def answer_detail(request, answer_id):
        answer_individual = answer.objects.get(pk=answer_id)
        return HttpResponse("<h1>Answer: %s <h1/>" % answer_individual.content)
    
#建立新問題，並將「使用者於form填入的資料」成立新資料
#def question_create(request):
    #    form = QuestionForm()
      #  return render_to_response('question_create.html',{'form': form}, context_instance=RequestContext(request))
    
def question_create(request):
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        question_new = question(subject=form.cleaned_data['subject'], publication_date=timezone.now())
                        question_new.save()
                        return redirect('/questions')
        else:
                form = QuestionForm()
        return render_to_response('question_create.html',{'form': form}, context_instance=RequestContext(request))
