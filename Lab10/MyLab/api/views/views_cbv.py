# from django.shortcuts import render
from rest_framework.decorators import APIView

from rest_framework.response import Response
# from rest_framework.request import Request

from api.models import Company, Vacancy

from api.serializers import CompanySerializer2, VacancySerializer2

from django.shortcuts import Http404

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        companies_json = CompanySerializer2(companies, many=True)
        return Response(companies_json.data)
    def post(self, request):
        # new_company = json.loads(request.body)
        serializer = CompanySerializer2(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CompanyDetailAPIView(APIView):
    def get_object(self, ind=None):
        try:
            return Company.objects.get(id = ind)
        except Company.DoesNotExist as dnee:
            # return Response({'message': str(dnee)})
            raise Http404
    def get(self, request, ind=None):
        company = self.get_object(ind)
        output = CompanySerializer2(company)
        return Response(output.data)
    def put(self, request, ind):
        company = self.get_object(ind)
        output = CompanySerializer2(instance=company, data = request.data)
        if output.is_valid():
            output.save()
            return Response(output.data)
        return Response (output.errors)
    def delete(self, request, ind):
        company = self.get_object(ind)
        company.delete()
        return Response({'message': 'Company was deleted'})

class CompanyShowVacanciesAPIView(APIView): #by default request is get
    def get_object(self, ind=None):
        try:
            company = Company.objects.get(id = ind)
            vacancies = company.vacancy_set.all()
            vacancies_json = VacancySerializer2(vacancies, many=True)
            return Response(vacancies_json.data)
        except Company.DoesNotExist as dnee:
            raise Http404
    def get(self, request, ind=None):
        vacancies = self.get_object(ind)
        return Response(vacancies.data)
        # Response({'message': 'not here'})

class VacanciesListAPIView(APIView):
    def get_object(self):
        try:
            vacancies = Vacancy.objects.all()
            vacancies_json = VacancySerializer2(vacancies, many=True)
            return vacancies_json
        except:
            Response({'message': 'err'})
    def get(self, request):
        vacancies = self.get_object()
        return Response(vacancies.data)
    def post(self, request):
        # my_data = json.loads(request.body)
        new_vacancy = VacancySerializer2(data = request.data)
        if new_vacancy.is_valid():
            new_vacancy.save()
            return Response(new_vacancy.data)
        return Response(new_vacancy.errors)
        # return JsonResponse('err', safe=False)

class VacancyDetailAPIView(APIView):
    def get_object(self, ind):
        try:
            return Vacancy.objects.get(id = ind)
        except Vacancy.DoesNotExist as dnee:
            raise Http404
    def get(self, request, ind):
        vacancy = self.get_object(ind)
        vacancy_json = VacancySerializer2(vacancy)
        return Response(vacancy_json.data)
    def put(self, request, ind):
        vacancy = self.get_object(ind)
        new_data = VacancySerializer2(vacancy, request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(new_data.data)
        return Response(new_data.errors)
    def delete(self, request, ind):
        vacancy = self.get_object(ind)
        vacancy.delete()
        return Response({'message': 'deleted successfully'})

class TopTenVacancies(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        vacancies_json = VacancySerializer2(vacancies, many=True)
        return Response(vacancies_json.data)
