from seeding.seeders import *
from advice.models import Advice
from statics.models import *
from seeder.seeders_data import advice, specialization, patient, doctor, superuser
from seeder.serializers import *


@SeederRegistry.register
class SuperuserSeeder(SerializerSeeder):
    serializer_class = SuperuserSeederSerializer
    data = superuser.data
    priority = 0
    id = 'SuperuserSeeder'


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
    csv_file_path = 'seeder/seeders_data/country.csv'
    priority = 0
    id = 'CountrySeeder'


@SeederRegistry.register
class CitySeeder(CSVFileModelSeeder):
    model = City
    csv_file_path = 'seeder/seeders_data/city.csv'
    priority = 1
    id = 'CitySeeder'


# @SeederRegistry.register
class DoctorSeeder(SerializerSeeder):
    serializer_class = DoctorSeederSerializer
    data = doctor.data
    priority = 1
    id = 'DoctorSeeder'


# @SeederRegistry.register
class PatientSeeder(SerializerSeeder):
    serializer_class = PatientSeederSerializer
    data = patient.data
    priority = 1
    id = 'PatientSeeder'


class ConsultationSeeder(SerializerSeeder):
    serializer_class = None
    data = 'adsf'
    priofity = 2
    id = 'ConsultationSeeder'


class ReviewSeeder(SerializerSeeder):
    serializer_class = None
    data = 'asdf'
    priofity = 2
    id = 'ReviewSeeder'

