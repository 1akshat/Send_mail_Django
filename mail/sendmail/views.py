from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from models import EmailForm

def sendmail(request):
	if request.POST:
	    form = EmailForm(request.POST)
	    if form.is_valid():
	      	firstname = form.cleaned_data['firstname']
	      	lastname = form.cleaned_data['lastname']
	      	email = form.cleaned_data['email']
	      	subject = form.cleaned_data['subject']
	      	message = form.cleaned_data['message']
	    	try:
	    		send_mail('subject', 'message', '<SENDER EMAIL ID>', ['<RECEIVER EMAIL ID"S>'])
	      		return HttpResponseRedirect('/email/thankyou/')
	    	except Exception, e:
	      		return HttpResponse('Except Block executed.' + str(e))
	    else:
	    	return HttpResponse("Form not Valid")
  	else:
  		return HttpResponseRedirect('/email/')  
