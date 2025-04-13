from django.shortcuts import render
from django.http import JsonResponse
from api.models import Company, Vacancy

def show_companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe = False)

def show_company(request, ind):
    try:
        company = Company.objects.get(id = ind)
    except Company.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})
    return JsonResponse(company.to_json())

def show_company_vacancies(request, ind):
    try:
        company = Company.objects.get(id = ind)
        vacancies = company.vacancy_set.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})
    # return JsonResponse({'message': 'ok'})
    return JsonResponse(vacancies_json, safe=False)

def show_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def show_vacancy(request, ind):
    try:
        vacancy = Vacancy.objects.get(id = ind)
    except Vacancy.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})
    return JsonResponse(vacancy.to_json())

def show_top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


# Create your views here.
