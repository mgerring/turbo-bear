from django.core.cache import cache
from django.utils.cache import get_cache_key
from django.http import HttpRequest
from csv import DictReader
import lopa
import ipdb

def _cache_key(path):
	request 	 = HttpRequest()
	request.path = path
	return get_cache_key(request)

def expire_cache(path):
	key = _cache_key(path)
	if cache.has_key(key):
		cache.delete(key)

def cache_status(path):
	key = _cache_key(path)
	if cache.has_key(key):
		print "cache hit"
	else:
		print "cache miss"

def load_zipcodes():
	# This is a one-time use function to generate
	# our ZIP code database from a CSV. This only needs
	# to be run once every time the ZIP database
	# is updated, and should be done using fixtures
	# otherwise.
	zipcode_database = open('db/free-zipcode-database.csv')
	reader = DictReader(zipcode_database)
	fucked = []
	for item in reader:
		if item['Decommisioned'] == 'false':
			zipcode = lopa.signatures.models.ZipCode()
			zipcode.zipcode = item['Zipcode']
			zipcode.state 	= item['State']
			zipcode.lat 	= item['Lat']
			zipcode.lon		= item['Long']
			try:
				zipcode.save()
			except:
				fucked.append(item)
