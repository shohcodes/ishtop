from rest_framework.routers import DefaultRouter

from api.professions.views import ProfessionAreaViewSet, ProfessionViewSet
from api.vacancies.views import VacancyViewSet

router = DefaultRouter()
router.register('profession_areas', ProfessionAreaViewSet, 'profession_areas')
router.register('professions', ProfessionViewSet, 'professions')
router.register('vacancies', VacancyViewSet, 'vacancies')

urlpatterns = router.urls
