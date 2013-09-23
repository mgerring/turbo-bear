from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from lopa.signatures.forms import *
from lopa.signatures.models import *
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page, never_cache
from lopa.signatures.util import cache_status
from django.views.decorators.cache import cache_control
from django.core import serializers
import json

class CreateSignature(CreateView):
	form  = SignatureForm
	model = Signature

	def get_success_url(self):
		return reverse('create')

class IndexSignatures(ListView):
	model 	= Signature

@cache_control(no_cache=True, max_age=1, must_revalidate=True)
@cache_page(60 * 60 * 24)
def count_signatures(request):
	count 	= Signature.objects.count()

	# The leaderboard query is a little complicated - if states have the
	# same number of votes, they should be in the same "place", which
	# means first we need to grab the three highest numbers of votes.

	# "Three top vote-getting states" stops making sense as soon as, say,
	# three states have the same number of votes. Which ones show up on the
	# leaderboard? Do you sort them alphabetically?
	counts = StateCount.objects.values_list('count', flat=True).order_by('-count').distinct()[:3]
	states = StateCount.objects.filter(count__in=counts).order_by('-count')
	state_list = {}

	for state in states:
		state_list[state.count] = state.state

	states	= [{'state':state.state, 'count':state.count} for state in states]
	json_string = json.dumps({'count':count,'states':states})
	return HttpResponse(json_string, mimetype="application/json")