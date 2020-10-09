from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView, UpdateView, ListView
from .serializers import CandidateResult, CandidateResultSerializer
from .forms import AddMarkForm
from .models import Grade
from .models import Candidate


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
        except Exception:
            return HttpResponse("Task already graded for this candidate")

        return super().form_valid(form)


def candidates_results(request):
    candidates = Candidate.objects.all()
    results = []
    for candidate in candidates:
        grades = [g.value for g in Grade.objects.filter(candidate__exact=candidate)]
        results.append(CandidateResult(candidate.pk, candidate, grades))
    serializer = CandidateResultSerializer(results, many=True)
    return JsonResponse({'data': serializer.data}, safe=False)
