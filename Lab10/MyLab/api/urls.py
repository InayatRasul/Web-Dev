from django.urls import path
# from api.views import show_companies, show_company, show_company_vacancies, show_vacancies, show_vacancy, show_top_ten_vacancies
from api.views import show_companies, show_company, show_company_vacancies, show_vacancies, show_vacancy, show_top_ten_vacancies, CompanyListAPIView, CompanyDetailAPIView, CompanyShowVacanciesAPIView, VacanciesListAPIView, VacancyDetailAPIView, TopTenVacancies
# urlpatterns = [
#     path('companies/', show_companies),
#     path('companies/<int:ind>/', show_company),
#     path('companies/<int:ind>/vacancies/', show_company_vacancies),
#     path('vacancies/',show_vacancies),
#     path('vacancies/<int:ind>', show_vacancy),
#     path('vacancies/top_ten', show_top_ten_vacancies)
# ]

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:ind>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:ind>/vacancies/', CompanyShowVacanciesAPIView.as_view()),
    path('vacancies/',VacanciesListAPIView.as_view()),
    path('vacancies/<int:ind>', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten', TopTenVacancies.as_view())
]