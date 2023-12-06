from sat.models import Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Company
        fields = ('id','company_name', 'description', 'number_of_employees')
    def save(self, user):
        self.validated_data['owner'] = user
        return super(CompanySerializer, self).save()

class CompanyDetailSerializer(serializers.ModelSerializer):  # create class to serializer model
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'description',"owner", "number_of_employees"]
