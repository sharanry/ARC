# from django.shortcuts import render


from django.http import HttpResponse
from django.contrib.auth.models import User

import csv
from tablib import Dataset

from main.resources import StudentResource
# Create your views here.


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list(
        'username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response


def simple_upload(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = student_resource.import_data(
            dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(
                dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')


def export(request):
    person_resource = StudentResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response