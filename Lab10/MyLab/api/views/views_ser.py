from django.shortcuts import render
from django.http import JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from django.views.decorators.csrf import csrf_exempt

import json
@csrf_exempt
def show_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = CompanySerializer(companies, many=True)
        return JsonResponse(companies_json.data, safe=False)
    elif request.method == 'POST':
        new_company = json.loads(request.body)
        serializer = CompanySerializer(data = new_company)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def show_company(request, ind):
    try:
        company = Company.objects.get(id = ind)
    except Company.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})
    if request.method == 'GET':
        output = CompanySerializer(company)
        return JsonResponse(output.data)
    elif request.method == 'PUT':
        dta = json.loads(request.body)
        output = CompanySerializer(instance=company, data = dta)
        if output.is_valid():
            output.save()
            return JsonResponse(output.data)
        return JsonResponse (output.errors)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'Company was deleted'})

def show_company_vacancies(request, ind):
    try:
        company = Company.objects.get(id = ind)
        vacancies = company.vacancy_set.all()
        vacancies_json = VacancySerializer(vacancies, many=True)
        return JsonResponse(vacancies_json.data, safe=False)
    except Company.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})

@csrf_exempt
def show_vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = VacancySerializer(vacancies, many=True)
    except:
        JsonResponse({'message': 'err'})
    if request.method == 'GET':
        return JsonResponse(vacancies_json.data, safe=False)
    elif request.method == 'POST':
        my_data = json.loads(request.body)
        new_vacancy = VacancySerializer(data = my_data)
        if new_vacancy.is_valid():
            new_vacancy.save()
            return JsonResponse(new_vacancy.data)
        return JsonResponse(new_vacancy.errors)
        # return JsonResponse('err', safe=False)

@csrf_exempt
def show_vacancy(request, ind):
    try:
        vacancy = Vacancy.objects.get(id = ind)
    except Vacancy.DoesNotExist as dnee:
        return JsonResponse({'message': str(dnee)})
    if request.method == 'GET':
        vacancy_json = VacancySerializer(vacancy)
        return JsonResponse(vacancy_json.data)
    elif request.method == 'PUT':
        my_data = json.loads(request.body)
        new_data = VacancySerializer(vacancy, my_data)
        if new_data.is_valid():
            new_data.save()
            return JsonResponse(new_data.data)
        return JsonResponse(new_data.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted successfully'})

def show_top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = VacancySerializer(vacancies, many=True)
    return JsonResponse(vacancies_json.data, safe=False)


# Create your views here.
