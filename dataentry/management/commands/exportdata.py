import csv
import datetime

from django.core.management.base import BaseCommand
from django.apps import apps



# commmand --> python manage.py exportdata model_name

class Command(BaseCommand):
    help = "export data from database to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **options):
        model_name = options['model_name'].capitalize()

        # search through all the installed apps for the model
        model = None
        for app_config  in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError as error:
                continue

        if not model:
            self.stderr.write(f'Model {model_name} cound not found')
            return

        # fetch the data from the database
        data = model.objects.all()

        # generate timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # define the csv file name(path
        file_path =f'exported_{model_name}_data_{timestamp}.csv'

        # open de csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer =csv.writer(file)

            # write the CSV header
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported succesfully!'))