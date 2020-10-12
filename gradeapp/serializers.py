from statistics import mean, StatisticsError

from rest_framework import serializers


class CandidateResult:
    def __init__(self, pk, full_name, grades):
        self.avg_grade = 0
        self.pk = pk
        self.full_name = full_name
        self.grades = grades
        self.update_average()


    def update_average(self):
        try:
            self.avg_grade = mean(self.grades)
        except StatisticsError:
            pass

    def __str__(self):
        return f'{self.avg_grade}'


class CandidateResultSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    full_name = serializers.CharField(max_length=200)
    avg_grade = serializers.FloatField()
    grades = serializers.ListField()
