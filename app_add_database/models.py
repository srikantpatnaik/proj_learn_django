from django.db import models
from django.forms import ModelForm

class add_db(models.Model):
	field1 = models.IntegerField(max_length=10000)
	field2 = models.IntegerField(max_length=10000)

class model_to_form(ModelForm):
	class Meta:
		model = add_db

