from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect , Http404 , HttpResponse
#from django.template import loader
from django.urls import reverse

from .form import SignupForm , LoginForm
from django.contrib.auth import authenticate,login as auth , logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Question , Choice
from django.views import generic
from django.utils import timezone


class IndexView(LoginRequiredMixin,generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	login_url = 'login/'
	redirect_field_name = 'redirect_to'
	
    

	#def get_queryset(self):
	#	return Question.objects.order_by('-pub_date')[:5]

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'	

	#get queryset testing ------------ 
	
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())
	

class ResultView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
	    return render(request,'polls/detail.html',{
	    	'question':question , 
	    	'error_message':"you didn't select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
	









def signup(request):
	if request.method=="POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('polls:login'))
	else:
		form = SignupForm()
	form = SignupForm()
	return render(request,'polls/signup.html',{'form':form})
def login(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username = username , password=password)
		if user is not None:
			auth(request,user)
			return HttpResponseRedirect(reverse('polls:index'))
	else:
		form = LoginForm()
	form = LoginForm()
	return render(request,'polls/login.html',{'form':form})
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('polls:login'))



"""
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
	    'latest_question_list':latest_question_list,
	}
	#output = ','.join([q.question_text for q in latest_question_list])
	#return HttpResponse(template.render(context,request)
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	'''
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExitst:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question':question})
	'''
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})     

def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id) 
	return render(request,'polls/results.html',{'question':question})

"""

