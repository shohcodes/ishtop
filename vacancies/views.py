from django.core.paginator import Paginator
from django.shortcuts import render

from professions.models import ProfessionArea, Profession
from vacancies.models import Vacancy


def get_vacancies(request):
    per_page = 6
    search = request.GET.get("search", "")
    profession_area = request.GET.get("profession_area", "0")
    profession = request.GET.get("profession", "0")
    page = request.GET.get("page", 1)

    profession_areas = ProfessionArea.objects.all()
    professions = Profession.objects.filter(profession_area_id=profession_area)

    page_obj = get_objects(
        page=page,
        per_page=per_page,
        profession_area_id=int(profession_area),
        profession_id=int(profession)
    )

    context = {
        "profession_areas": profession_areas,
        "professions": professions,
        "page_obj": page_obj,
        "search": search,
        "profession": int(profession),
        "profession_area": int(profession_area)
    }
    return render(request, "vacancies.html", context)


def get_objects(page, per_page=25, profession_area_id=None, profession_id=None, ):
    filters = {
        "is_active": True,
    }
    if profession_id:
        filters["profession_id"] = profession_id
    else:
        if profession_area_id:
            filters["profession__profession_area_id"] = profession_area_id

    vacancies = Vacancy.objects.filter(
        **filters
    ).order_by(
        "-created_at", "-updated_at"
    )
    print(filters, vacancies)
    paginator = Paginator(vacancies, per_page)
    page_obj = paginator.get_page(page)
    return page_obj
