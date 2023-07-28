import abc
from django.db import models
from django.conf import settings
from django.http import HttpRequest
from rest_framework import serializers
from seeding.models import AppliedSeeder

class Seeder(abc.ABC):
    @abc.abstractmethod
    def seed(self):
        pass
    
    def _seed(self):
        name = str(type(self))

        GREEN_COLOR = "\033[32m"
        # RED_COLOR = "\033[31m"
        WHITE_COLOR = "\033[0m"

        if self._get_just_debug() and not settings.DEBUG:
            # print(RED_COLOR + name + " is just_debug (isn't applied) " + WHITE_COLOR)
            return
        
        if AppliedSeeder.objects.filter(name=name).exists():
            # print(RED_COLOR + name + " is already exists in the DataBase " + WHITE_COLOR)
            return
        
        self.seed()
        AppliedSeeder.objects.create(name=name)
        print(GREEN_COLOR + name + " is applied successfully ^_^ " + WHITE_COLOR)

    def get_priority(self):
        return getattr(self, 'priority', float('inf'))
    
    def _get_priority(self):
        priority = self.get_priority()

        if not isinstance(priority, float) and not isinstance(priority, int):
            raise TypeError('priority must be a number')
        
        return priority

    def get_just_debug(self):
        return getattr(self, 'just_debug', False)
    
    def _get_just_debug(self):
        just_debug = self.get_just_debug()

        if not isinstance(just_debug, bool):
            raise TypeError('just_debug must be bool value')
        
        return just_debug

class DataSeeder(Seeder):
    def get_data(self):
        data = getattr(self, 'data', None)

        if data is None:
            raise TypeError('subclasses of DataSeeder must have data class property or the get_data method')
        
        return data
    
    def _get_data(self):
        data = self.get_data()

        error_message = 'data must be list of dict'

        if not isinstance(data, list):
            raise TypeError(error_message)
        
        for record_data in data:
            if not isinstance(record_data, dict):
                raise TypeError(error_message)
        
        return data

class ModelSeeder(DataSeeder):
    def get_model(self):
        model = getattr(self, 'model', None)

        if model is None:
            raise TypeError('subclasses of ModelSeeder must have model class property or the get_model method')
        
        return model
    
    def _get_model(self):
        model = self.get_model()

        if not isinstance(model, type) or not issubclass(model, models.Model):
            raise TypeError('model must be a subclasse of django.db.models.Model')
        
        return model

    def seed(self):
        data = self._get_data()
        model = self._get_model()
        new_objects = []
        for record_data in data:
            new_objects.append(model(**record_data))
        model.objects.bulk_create(new_objects)
    

class SerializerSeeder(DataSeeder):
    def get_serializer_class(self):
        serializer_class = getattr(self, 'serializer_class', None)

        if serializer_class is None:
            raise TypeError('subclasses of SerializerSeeder must have serializer_class class property or the get_serializer_class method')
        
        return serializer_class
    
    def _get_serializer_class(self):
        serializer_class = self.get_serializer_class()

        if not isinstance(serializer_class, type) or not issubclass(serializer_class, serializers.Serializer):
            raise TypeError('serializer_class must be a subclasse of rest_framework.serializers.Serializer')
        
        return serializer_class
    
    def seed(self):
        data = self._get_data()
        serializer_class = self._get_serializer_class()
        for record_data in data:
            request = HttpRequest()
            request.user = None
            serializer = serializer_class(data=record_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        

class EmptySeeder(ModelSeeder):
    def get_records_count(self):
        records_count = getattr(self, 'records_count', None)

        if records_count is None:
            raise TypeError('subclasses of EmptySeeder must have records_count class property or the get_records_count method')
        
        return records_count
    
    def _get_records_count(self):
        records_count = self.get_records_count()

        if not isinstance(records_count, int):
            raise TypeError('records_count must be int')
        
        return records_count
    
    def get_data(self):
        return [ {} for _ in range(self._get_records_count()) ]
    

class CSVFileReader():
    def get_csv_file_path(self):
        csv_file_path = getattr(self, 'csv_file_path', None)

        if csv_file_path is None:
            raise TypeError('subclasses of CSVFileReader must have csv_file_path class property or the get_csv_file_path method')
        
        return csv_file_path
    
    def _get_csv_file_path(self):
        csv_file_path = self.get_csv_file_path()

        if not isinstance(csv_file_path, str):
            raise TypeError('csv_file_path must be str')
        
        return csv_file_path
    
    def get_data(self):
        data = []
        csv_file_path = self._get_csv_file_path()
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            labels = []
            for values in file:
                values = [value.strip() for value in values.split(',')]
                if not labels:
                    labels = values
                else:
                    record_data = { label: value for label, value in zip(labels, values) }
                    data.append(record_data)
        return data
    
    
class CSVFileModelSeeder(CSVFileReader, ModelSeeder):
    pass
    
    
class CSVFileSerializerSeeder(CSVFileReader, SerializerSeeder):
    pass
    

class SeederRegistry:
    seeders = []

    @classmethod
    def register(cls, seeder):
        if not issubclass(seeder, Seeder):
            raise TypeError('Only subclasses of Seeder class can be registered with SeederRegistry.register')
        cls.seeders.append(seeder())

    @classmethod
    def seed_all(cls):
        cls.seeders.sort(key=lambda seeder: seeder._get_priority())
        for seeder in cls.seeders:
            seeder._seed()

