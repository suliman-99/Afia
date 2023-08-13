import secrets
import datetime
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
        

@SeederRegistry.register
class DoctorExperience(Seeder):
    priority = 4
    id = 'DoctorExperience'

    def seed(self):
        hospitals = {
            'Damascus': [
                'Al-Mouwasat Hospital',
                'Ibn Al-Nafis Hospital',
                'Tishreen Military Hospital',
                'Al-Shami Hospital',
                'Al-Assad University Hospital',
                'Ibn Al-Jazzar Hospital',
                'Syrian Arab Red Crescent Hospital',
                'Al-Mujtahid Hospital',
                'Syrian French Hospital',
                'Al-Asadi Medical Center',
                'Al-Bassel Heart Institute',
                'Al-Awael Medical Center',
                'Al-Razi Hospital',
                'Al-Mowasat Private Hospital',
                'Al-Salam Hospital',
                'Al-Noor Hospital',
                'Hajjar Hospital',
                'Al-Rawabi Hospital',
                'Al-Afdal Hospital',
                'Al-Hayat Hospital'
            ],
            'Homs': [
                'Al-Birr and Al-Safwa Hospital',
                'National Hospital',
                'Al-Amal Hospital',
                'Al-Watany Hospital',
                'Al-Bourj Hospital',
                'Ibn Al-Jazzar Hospital',
                'Al-Nour Hospital',
                'Al-Bassel Heart Institute',
                'Al-Furat Hospital',
                'Homs Military Hospital',
                'Al-Hayat Hospital',
                'Tal Kalakh Hospital',
                'Al-Qusair Hospital',
                'Talbiseh Hospital',
                'Al-Qalamoun Hospital',
                'Homs Central Hospital',
                'Al-Bassel Hospital for Children',
                'Al-Ghouta Hospital',
                'Al-Saddiq Hospital',
                'Al-Moallem Hospital'
            ],
            'Aleppo': [
                'Al-Razi Hospital',
                'University Hospital of Aleppo',
                'Al-Shifaa Hospital',
                'Al-Mouwasat Hospital',
                'Al-Ittihad Hospital',
                'Al-Bassel Hospital',
                'Al-Jamiliyah Hospital',
                'Al-Mukharram Hospital',
                'Ibn Khaldoun Hospital',
                'Al-Zahrawi Hospital',
                'Al-Watany Hospital',
                'Al-Sham Hospital',
                'Al-Wataniya Hospital',
                'Dar Al-Shifa Hospital',
                'Al-Qadi Askar Hospital',
                'Al-Salama Hospital',
                'Al-Mansoura Hospital',
                'Al-Rajaa Hospital',
                'Al-Karamah Hospital',
                'Ibn Al-Nafees Hospital'
            ]
        }
        doctors:list[User] = list(User.objects.filter(role=User.ROLE_DOCTOR))
        for doctor in doctors:
            doctor.birth_date = datetime.datetime.strptime(f'{secrets.randbelow(16)+1970}-{secrets.randbelow(12)+1}-{secrets.randbelow(28)+1}', '%Y-%m-%d')
            graduation_year = doctor.birth_date.year + 27
            city_name = doctor.city.name
            city_hospitals = hospitals.get(city_name, [])
            if not city_hospitals:
                continue
            hospital = city_hospitals[secrets.randbelow(len(city_hospitals))]
            doctor.experience = f'{doctor.specialization} specialized since {graduation_year} in {hospital}'
        User.objects.bulk_update(doctors, ['birth_date', 'experience'])
        

