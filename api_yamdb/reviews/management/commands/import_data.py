import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, User


Models = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles_v1.csv',
}


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        answer = input('Очистить базу перед импортом? [Y/N]: ')
        yes = ['Y', 'y']
        no = ['N', 'n']
        if answer in yes:
            User.objects.all().delete()
            Category.objects.all().delete()
            Genre.objects.all().delete()
            Title.objects.all().delete()
        elif answer in no:
            return ('Лучше воспользоваться admin панелью')
        elif answer not in yes or no:
            return ('Incorrect answer')

        for model, csv_files in Models.items():
            with open(
                f'{settings.STATICFILES_DIRS[0]}/data/{csv_files}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(
                    model(**data) for data in reader
                )
            self.stdout.write(
                f'Данные для таблицы {model.__name__} успешно загружены')
