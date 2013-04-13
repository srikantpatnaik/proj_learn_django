# Create your views here.
from django.shortcuts import render_to_response
from forms import Output
from django.template import RequestContext


def app_add(request):
    form = Output()
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

