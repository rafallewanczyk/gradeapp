from statistics import mean

from rest_framework import serializers


class CandidateResult:
    def __init__(self, pk, full_name, grades):
        self.pk = pk
        self.full_name = full_name
        self.grades = grades
        self.avg_grade = mean(self.grades)


class CandidateResultSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    full_name = serializers.CharField(max_length=200)
    avg_grade = serializers.FloatField()
    grades = serializers.ListField()
