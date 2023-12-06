from django_filters import rest_framework as filters
from .models import Company


# We create filters for each field we want to be able to filter on
class CompanyFilter(filters.FilterSet):
    company_name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    number_of_employees = filters.NumberFilter()
    number_of_employees__gt = filters.NumberFilter(field_name='number_of_employees', lookup_expr='gt')
    number_of_employees__lt = filters.NumberFilter(field_name='number_of_employees', lookup_expr='lt')
    class Meta:
        model = Company
        fields = ['company_name', 'description', 'number_of_employees', 'number_of_employees__gt', 'number_of_employees__lt']