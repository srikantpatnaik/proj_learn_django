# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import model_to_form

def app_add_database(request):
    form_db = model_to_form()
    if request.method == 'POST':
        form_db = model_to_form(request.POST)
        if form_db.is_valid():
            clean_form = form_db.cleaned_data
            value1 = clean_form['field1']
            value2 = clean_form['field2']
            out = value1 + value2
            form_db.save()
            return render_to_response('add_db.html', {'calculator':form_db, 'answer':out}, context_instance = RequestContext(request))
        else:
			return render_to_response('add_db.html', {'calculator':form_db}, context_instance = RequestContext(request))
    else:
	    return render_to_response('add_db.html', {'calculator':form_db}, context_instance = RequestContext(request))

