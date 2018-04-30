import operator
# import requests
from django.shortcuts import render, redirect

from django.views.generic import ListView

from .models import Subject




from django.db.models import Q

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'
    context_object_name = 'subjects'


class SubjectSearchListView(SubjectListView):
    """
    Display a Blog List page filtered by the search query.
    """
    # paginate_by = 10

    def get_queryset(self):
        result = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list))
            )

        return result

def home(request):
    return render(request, 'home.html', {})
