from django.db import models

from professions.models import Profession
from users.models import User


class Vacancy(models.Model):
    owner = models.ForeignKey(User, related_name='vacancy_owner', on_delete=models.PROTECT)
    profession = models.ForeignKey(Profession, related_name='vacancy_profession', on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    description = models.TextField()
    salary_from = models.BigIntegerField(null=True)
    salary_to = models.BigIntegerField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.title}'
