from seeding.seeders import *
from advice.models import Advice
from statics.models import *
from seeder.seeders_data import advice, specialization


@SeederRegistry.register
class AdviceSeeder(ModelSeeder):
    model = Advice
    data = advice.data
    priority = 0
    id = 'AdviceSeeder'


@SeederRegistry.register
class SpecializationSeeder(ModelSeeder):
    model = Specialization
    data = specialization.data
    priority = 0
    id = 'SpecializationSeeder'


@SeederRegistry.register
class CountrySeeder(CSVFileModelSeeder):
    model = Country
    csv_file_path = 'seeder/seeders_data/Country.csv'
    priority = 0
    id = 'CountrySeeder'


@SeederRegistry.register
class CitySeeder(CSVFileModelSeeder):
    model = City
    csv_file_path = 'seeder/seeders_data/City.csv'
    priority = 1
    id = 'CitySeeder'

