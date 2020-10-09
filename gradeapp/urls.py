from django.urls import path
from . import views

app_name = 'gradeapp'

urlpatterns = [
    path('add-mark/', views.AddMarkView.as_view(), name='add-mark'),
    path('candidates/', views.candidates_results, name = 'candidates-result'),
]