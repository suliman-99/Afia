from seeding.seeders import *
from static.models import *


@SeederRegistry.register
class SpecializationSeeder(CSVFileModelSeeder):
    model = Specialization
    csv_file_path = 'seeder/seeders/Specialization.csv'
    priority = 0


@SeederRegistry.register
class CountrySeeder(CSVFileModelSeeder):
    model = Country
    csv_file_path = 'seeder/seeders/Country.csv'
    priority = 0


@SeederRegistry.register
class CitySeeder(CSVFileModelSeeder):
    model = City
    csv_file_path = 'seeder/seeders/City.csv'
    priority = 1

