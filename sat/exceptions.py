from rest_framework.exceptions import APIException

class MaxCompaniesAPIExecption(APIException):
    status_code = 400
    default_detail = 'Each user can have maximum of 5 companies'
    default_code = 'too_many_companies'