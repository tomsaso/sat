from sat.permissons import IsOwner
from sat.models import Company
from sat.serializers import CompanySerializer, CompanyDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from sat.pagination import CustomPagination
from sat.filters import CompanyFilter
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from sat.exceptions import MaxCompaniesAPIExecption
from django.core.mail import send_mail

class Companies(ListCreateAPIView):
    """
    List all companies or create a company
    """
    permission_classes = [IsOwner]
    serializer_class=CompanySerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,OrderingFilter)
    ordering_fields = '__all__'
    filterset_class = CompanyFilter
    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user).all()
    def perform_create(self, serializer):
        user= self.request.user
        if user.companies.count()>=5:
            raise MaxCompaniesAPIExecption
        serializer.save(user=user)
        company = serializer.validated_data['company_name']
        send_mail(
            subject=f"Company {company} created!",
            message=f"You have sucessfuly added company {company}  to your ownership.",
            from_email="notifybotibrkfut@outlook.com",
            recipient_list=[user.email],
            fail_silently=False
        )

class CompanyDetail(RetrieveUpdateAPIView):
    """
    Get company detail by PK or update (PATCH) number_of_employees
    """
    permission_classes = [IsOwner]
    lookup_field = "pk"
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
