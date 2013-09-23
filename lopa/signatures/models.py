from django.db import models
from lopa.signatures.util import expire_cache
from django.core.urlresolvers import reverse
from collections import defaultdict
import ipdb

class Signature(models.Model):
	name 		= models.CharField(max_length=256)
	email 		= models.EmailField(max_length=254 ) #why 254 --> https://docs.djangoproject.com/en/dev/ref/models/fields/#emailfield
	subscribe 	= models.BooleanField()
	zipcode		= models.CharField(max_length=10)

	def save(self):
		super(Signature, self).save()
		try:
			zipcode = ZipCode.objects.get(zipcode = self.zipcode)
		except:
			zipcode = False

		if zipcode:
			state, created 	= StateCount.objects.get_or_create(state = zipcode.state, defaults = {'count':0})
			state.count = state.count + 1
			state.save()

		expire_cache( '/count' )

class ZipCode(models.Model):
	zipcode = models.CharField(max_length=10, unique=True)
	state 	= models.CharField(max_length=2)
	lat 	= models.DecimalField(max_digits=5, decimal_places=2)
	lon 	= models.DecimalField(max_digits=5, decimal_places=2)

class StateCountManager(models.Manager):
	def leaderboard(self):
		# The leaderboard query is a little complicated - if states have the
		# same number of votes, they should be in the same "place", which
		# means first we need to grab the three highest numbers of votes, then
		# grab all states having those vote numbers, then group and sort the result
		counts = self.values_list('count', flat=True).order_by('-count').distinct()[:3]
		states = self.filter(count__in=counts)
		state_list = defaultdict(list)
		for state in states:
			state_list[state.count].append(state.state)
		return sorted([(key, value) for key, value in state_list.iteritems()], key=lambda state: state[0], reverse=True)

class StateCount(models.Model):
	state 	= models.CharField(max_length=2)
	count 	= models.IntegerField()
	objects = StateCountManager()
