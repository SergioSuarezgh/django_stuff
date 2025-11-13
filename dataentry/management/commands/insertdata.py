from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'insert data to the database'

    def handle(self, *args, **kwargs):

        dataset = [
            {'roll_no': 1002, 'name': 'Eva', 'age': 20},
            {'roll_no': 1003, 'name': 'Gara', 'age': 20},
            {'roll_no': 1004, 'name': 'Isa', 'age': 20},
            {'roll_no': 1005, 'name': 'Noe', 'age': 20}
        ]

        for data in dataset:
            roll_no = data["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no = data["roll_no"], name=data["name"], age=data["age"])
            else:
                self.stdout.write(self.style.WARNING(f'Stundent roll_no;{roll_no} exists!'))

        #Student.objects.create(roll_no= 1001, name='Sergio', age=20)
        self.stdout.write(self.style.SUCCESS('Data inserted succesfuly!'))
