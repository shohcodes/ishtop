from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.permissions import IsSuperUser
from vacancies.filters import VacancyFilter
from vacancies.models import Vacancy
from vacancies.serializers import VacancySerializer


class VacancyViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [IsSuperUser]
    filter_backends = [VacancyFilter]


