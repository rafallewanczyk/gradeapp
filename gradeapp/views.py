from collections import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView, UpdateView, ListView
from .serializers import CandidateResult, CandidateResultSerializer
from .forms import AddMarkForm
from .models import Grade
from .models import Candidate
from django.db import IntegrityError


class AddMarkView(FormView):
    template_name = 'gradeapp/add_mark.html'
    form_class = AddMarkForm
    success_url = '/api/add-mark'

    def form_valid(self, form):
        candidate = form.cleaned_data['candidate']
        recruiter = form.cleaned_data['recruiter']
        value = form.cleaned_data['value']
        task = form.cleaned_data['task']

        query = Grade(candidate=candidate, value=int(value), recruiter=recruiter, task=task)
        try:
            query.save()
        except IntegrityError:
            return HttpResponse("Task already graded for this candidate", status=409)

        return super().form_valid(form)


def candidates_results(request):
    candidates = Candidate.objects.all()
    grades = Grade.objects.all()

    dictionary = OrderedDict()
    for candidate in candidates:
        dictionary[candidate] = CandidateResult(candidate.pk, candidate, [])

    for g in grades:
        dictionary[g.candidate].grades.append(g.value)

    for row in dictionary:
        dictionary.get(row).update_average()

    results = [dictionary.get(candidate) for candidate in dictionary]

    serializer = CandidateResultSerializer(results, many=True)
    return JsonResponse({'data': serializer.data}, safe=False)
