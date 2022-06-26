from django.db import models
from teachers.models import CustomUser


class Course(models.Model):
    name = models.CharField(max_length=150)
    chapters = models.IntegerField(default=0)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    correct_answer = models.IntegerField()
    difficulty = models.CharField(
        max_length=2,
        choices=[("SM", "Simple"), ("DF", "Difficult")])
    objective = models.CharField(
        max_length=2,
        choices=[("RM", "Reminding"), ("UD", "Understanding"), ("CR", "Creativity")])
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    
