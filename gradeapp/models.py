from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Recruiter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class Grade(models.Model):
    value = models.IntegerField(default= 0)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task}: {self.value} od {self.recruiter} dla {self.candidate}'

    class Meta:
        unique_together =('candidate', 'task')


