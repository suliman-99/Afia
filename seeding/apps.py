import sys
import importlib.util
from pathlib import Path
from django.apps import AppConfig
from django.apps import apps

class SeedingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seeding'

    def ready(self):

        for app_config in apps.get_app_configs():
            app_name = app_config.name
            module_name = 'seeders'
            file_name = module_name + '.py'
            file_path = Path(app_config.path) / file_name
            if file_path.exists():
                spec = importlib.util.spec_from_file_location(f"{app_name}.{module_name}", str(file_path))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
        
        if 'runserver' in sys.argv:
            from seeding.seeders import SeederRegistry
            SeederRegistry.seed_all()

        return super().ready()
