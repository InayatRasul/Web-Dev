from rest_framework import serializers

from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    
    def create(self,new_company):
        company = Company.objects.create(**new_company)
        return company
    
    def update(self, instance,new_data):
        instance.name = new_data['name']
        instance.description= new_data['description']
        instance.city = new_data['city']
        instance.address = new_data['address']
        instance.save()
        return instance
class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = serializers.PrimaryKeyRelatedField(queryset = Company.objects.all())

    def create(self, new_vacancy):
        res = Vacancy.objects.create(**new_vacancy)
        return res
    def update(self, instance, new_data):
        instance.name = new_data['name']
        instance.description = new_data['description']
        instance.salary = new_data['salary']
        instance.company = new_data['company']
        instance.save()
        return instance
class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')

    

