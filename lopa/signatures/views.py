from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from lopa.signatures.forms import *
from lopa.signatures.models import *
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page, cache_control
from django.contrib import messages
import json

class CreateSignature(CreateView):
	form  = SignatureForm
	model = Signature

	def get_success_url(self):
		return reverse('create')

	def form_valid(self, form):
		messages.success(self.request, 'Signature succesfully added!')
		return super(CreateSignature, self).form_valid(form)

class IndexSignatures(ListView):
	model 	= Signature

# The cache control headers make sure browsers don't cache
# the result of the AJAX call, but the result *is* cached by
# Django.
@cache_control(no_cache=True, max_age=1, must_revalidate=True)
@cache_page(60 * 60 * 24)
def count_signatures(request):
	count 		= Signature.objects.count()
	states  	= StateCount.objects.leaderboard()
	json_string = json.dumps({'count':count,'states':states})
	return HttpResponse(json_string, mimetype="application/json")