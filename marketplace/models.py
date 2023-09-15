from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RequiredSkill(models.Model):
    required_skill = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.required_skill}'


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    required_skills = models.ManyToManyField(RequiredSkill)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.title}'
    