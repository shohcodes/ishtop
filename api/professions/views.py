from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from professions.models import ProfessionArea, Profession
from professions.serializers import ProfessionAreaSerializer, ProfessionSerializer
from users.permissions import IsSuperUser


class ProfessionAreaViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = ProfessionArea.objects.all()
    serializer_class = ProfessionAreaSerializer
    permission_classes = [IsSuperUser]


class ProfessionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [IsSuperUser]
