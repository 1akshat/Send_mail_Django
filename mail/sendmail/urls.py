from django.conf.urls import url, include
from django.conf import settings
from django.views.generic.base import TemplateView
from views import sendmail

urlpatterns = [
	url(r'^email/send/$', sendmail),
	url(r'^email/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
	url(r'^email/$', TemplateView.as_view(template_name='email.html'), name='email'),
]