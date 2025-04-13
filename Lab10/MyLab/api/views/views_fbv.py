# from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response
# from rest_framework.request import Request

from api.models import Company, Vacancy

from api.serializers import CompanySerializer2, VacancySerializer2

@api_view(['GET', 'POST'])
def show_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = CompanySerializer2(companies, many=True)
        return Response(companies_json.data)
    elif request.method == 'POST':
        # new_company = json.loads(request.body)
        serializer = CompanySerializer2(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def show_company(request, ind):
    try:
        company = Company.objects.get(id = ind)
    except Company.DoesNotExist as dnee:
        return Response({'message': str(dnee)})
    if request.method == 'GET':
        output = CompanySerializer2(company)
        return Response(output.data)
    elif request.method == 'PUT':
        # dta = json.loads(request.body)
        output = CompanySerializer2(instance=company, data = request.data)
        if output.is_valid():
            output.save()
            return Response(output.data)
        return Response (output.errors)
    elif request.method == 'DELETE':
        company.delete()
        return Response({'message': 'Company was deleted'})

@api_view(['GET',]) #should define default one 
def show_company_vacancies(request, ind): #by default request is get
    try:
        company = Company.objects.get(id = ind)
        vacancies = company.vacancy_set.all()
        vacancies_json = VacancySerializer2(vacancies, many=True)
        return Response(vacancies_json.data)
    except Company.DoesNotExist as dnee:
        return Response({'message': str(dnee)})

@api_view(['GET','POST'])
def show_vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = VacancySerializer2(vacancies, many=True)
    except:
        Response({'message': 'err'})
    if request.method == 'GET':
        return Response(vacancies_json.data)
    elif request.method == 'POST':
        # my_data = json.loads(request.body)
        new_vacancy = VacancySerializer2(data = request.data)
        if new_vacancy.is_valid():
            new_vacancy.save()
            return Response(new_vacancy.data)
        return Response(new_vacancy.errors)
        # return JsonResponse('err', safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def show_vacancy(request, ind):
    try:
        vacancy = Vacancy.objects.get(id = ind)
    except Vacancy.DoesNotExist as dnee:
        return Response({'message': str(dnee)})
    if request.method == 'GET':
        vacancy_json = VacancySerializer2(vacancy)
        return Response(vacancy_json.data)
    elif request.method == 'PUT':
        # my_data = json.loads(request.body)
        new_data = VacancySerializer2(vacancy, request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(new_data.data)
        return Response(new_data.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'message': 'deleted successfully'})

@api_view(['GET'])
def show_top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = VacancySerializer2(vacancies, many=True)
    return Response(vacancies_json.data)
