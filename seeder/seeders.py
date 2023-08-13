import secrets
from django.db.models.query_utils import Q
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
class SuperuserSeeder(CSVFileModelSeeder):
    model = User
    csv_file_path = 'seeder/seeders_data/superuser.csv'
    priority = 0
    id = 'SuperuserSeeder'


@SeederRegistry.register
class DoctorSeeder(CSVFileModelSeeder):
    model = User
    csv_file_path = 'seeder/seeders_data/doctor.csv'
    priority = 2
    id = 'DoctorSeeder'


@SeederRegistry.register
class PatientSeeder(CSVFileModelSeeder):
    model = User
    csv_file_path = 'seeder/seeders_data/patient.csv'
    priority = 2
    id = 'PatientSeeder'


@SeederRegistry.register
class UserDataSeeder(Seeder):
    priority = 3
    id = 'UserDataSeeder2'

    def seed(self):
        cities_data = [
            { 'name': 'Damascus', 'country_id': 'Syria', },
            { 'name': 'Homs', 'country_id': 'Syria', },
            { 'name': 'Aleppo', 'country_id': 'Syria', },
        ]
        filter = Q()
        for city_data in cities_data:
            filter |= Q(**city_data)
        cities = list(City.objects.filter(filter))
        specializations = list(Specialization.objects.all())
        users:list[User] = list(User.objects.all())
        male_doctors:list[User] = []
        female_doctors:list[User] = []
        male_patients:list[User] = []
        female_patients:list[User] = []
        for user in users:
            if user.role == User.ROLE_DOCTOR:
                if user.gender == User.GENDER_MALE:
                    male_doctors.append(user)
                else:
                    female_doctors.append(user)
            elif user.role == User.ROLE_PATIENT:
                if user.gender == User.GENDER_MALE:
                    male_patients.append(user)
                else:
                    female_patients.append(user)
        for idx, doctor in enumerate(male_doctors + female_doctors + male_patients + female_patients):
            doctor.email_verified = True
            doctor.city = cities[secrets.randbelow(len(cities))]
        for idx, doctor in enumerate(male_doctors + female_doctors):
            doctor.specialization = specializations[secrets.randbelow(len(specializations))]
        def make_photo_url(file_name):
            return f'users/photos/{file_name}.jpg'
        for idx, male_doctor in enumerate(male_doctors):
            male_doctor.photo = make_photo_url(f'md{secrets.randbelow(20)+1}')
        for idx, female_doctor in enumerate(female_doctors):
            female_doctor.photo = make_photo_url(f'fd{secrets.randbelow(20)+1}')
        for idx, male_patient in enumerate(male_patients):
            male_patient.photo = make_photo_url(f'mp{secrets.randbelow(20)+1}')
        for idx, female_patient in enumerate(female_patients):
            female_patient.photo = make_photo_url(f'fp{secrets.randbelow(20)+1}')
        User.objects.bulk_update(
            male_doctors + female_doctors + male_patients + female_patients, 
            [
                'email_verified',
                'city',
                'specialization',
                'photo',
            ]
        )
        
        

