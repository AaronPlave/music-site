from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'




#OLD WAY, NOT USING GENERIC VIEWS
# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	context = {'latest_poll_list': latest_poll_list}
# 	return render(request,'polls/index.html',context)
	
# def detail(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	return render(request, 'polls/results.html',{'poll':poll})

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		#request.POST is a dictionary-like object that lets you access 
		#submitted data by key name. In this case, request.POST['choice'] 
		#returns the ID of the selected choice, as a string. request.POST
		#values are always strings.
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll':p,
			'error_message': "You didn't select a choice.",
			})    
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Always return an HttpResponseRedirect after successfully dealing 
		#with POST data. THis prevents data from being posted twice if a user 
		#hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id)))

