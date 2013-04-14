# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from app_add_database.models import model_to_form

def app_add_database(request):
    form = model_to_form()
    if request.method == 'POST':
        form = Output(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            value1 = clean_form['input1']
            value2 = clean_form['input2']
            out = value1 + value2
            return render_to_response('add.html', {'calculator':form, 'answer':out}, context_instance = RequestContext(request))
        else:
			return render_to_response('add.html', {'calculator':form}, context_instance = RequestContext(request))
    else:
	    return render_to_response('add.html', {'calculator':form}, context_instance = RequestContext(request))

