from django.db import models
# Create your models here.
class Company(models.Model):
    company_name = models.CharField("Company Name","company_name", max_length=200)
    description = models.TextField("Description", "description")
    number_of_employees = models.IntegerField("Number of employees","number_of_employees")
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="companies")