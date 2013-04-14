from django.db import models
from django.forms import ModelForm

class add_db(models.Model):
	filed1 = models.IntegerField(max_length=10)
	filed2 = models.IntegerField(max_length=10)

class model_to_form(ModelForm):
	class Meta:
		model = add_db

# Create your models here.
