from lopa.signatures.models import *
from django.forms import ModelForm

class SignatureForm(ModelForm):
	class Meta:
		model = Signature
		fields = ('name', 'email', 'zipcode', 'subscribe')