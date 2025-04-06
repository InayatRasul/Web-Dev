from django.urls import path
from api.views import show_companies, show_company, show_company_vacancies, show_vacancies, show_vacancy, show_top_ten_vacancies

urlpatterns = [
    path('companies/', show_companies),
    path('companies/<int:ind>/', show_company),
    path('companies/<int:ind>/vacancies/', show_company_vacancies),
    path('vacancies/',show_vacancies),
    path('vacancies/<int:ind>', show_vacancy),
    path('vacancies/top_ten', show_top_ten_vacancies)
]