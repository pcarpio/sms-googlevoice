# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from googlevoice import Voice
from googlevoice.util import input


from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django.contrib import messages

def home (request):
	voice = Voice()
	voice.login ()

	phoneNumber = input ('Number to send message to:')
	text = input ('message text:')
	try:

		voice.send_sms (phoneNumber, text)
	except:
		return render_to_response('error.html', {}, context_instance=RequestContext(request))	
	
	return render_to_response('home.html', {}, context_instance=RequestContext(request))