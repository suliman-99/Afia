from seeding.seeders import *
from advice.models import Advice
from statics.models import *
from seeder.serializers import *


@SeederRegistry.register
class AdviceSeeder(CSVFileModelSeeder):
    model = Advice
    csv_file_path = 'seeder/seeders_data/advice.csv'
    priority = 0
    id = 'AdviceSeeder'


@SeederRegistry.register
class SpecializationSeeder(CSVFileModelSeeder):
    model = Specialization
    csv_file_path = 'seeder/seeders_data/specialization.csv'
    priority = 0
    id = 'SpecializationSeeder'


@SeederRegistry.register
class CountrySeeder(CSVFileModelSeeder):
    model = Country
    csv_file_path = 'seeder/seeders_data/country.csv'
    priority = 0
    id = 'CountrySeeder'


@SeederRegistry.register
class CitySeeder(CSVFileModelSeeder):
    model = City
    csv_file_path = 'seeder/seeders_data/city.csv'
    priority = 1
    id = 'CitySeeder'


@SeederRegistry.register
class SuperuserSeeder(CSVFileSerializerSeeder):
    serializer_class = SuperuserSeederSerializer
    csv_file_path = 'seeder/seeders_data/superuser.csv'
    priority = 0
    id = 'SuperuserSeeder'


@SeederRegistry.register
class DoctorSeeder(CSVFileSerializerSeeder):
    serializer_class = DoctorSeederSerializer
    csv_file_path = 'seeder/seeders_data/doctor.csv'
    priority = 2
    id = 'DoctorSeeder'


@SeederRegistry.register
class PatientSeeder(CSVFileSerializerSeeder):
    serializer_class = PatientSeederSerializer
    csv_file_path = 'seeder/seeders_data/patient.csv'
    priority = 2
    id = 'PatientSeeder'

