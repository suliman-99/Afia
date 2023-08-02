import sys
import importlib.util
from pathlib import Path
from django.apps import AppConfig
from django.apps import apps

class SeedingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seeding'

    def ready(self):
        """
        import all `seeders.py` files in the installed apps to register them in the `SeederRegistry` class

        Note: the decorator `@SeederRegistry.register` will be applied when the file is imported

        so, if the seeder class is written in another file (not in `seeders.py`)
        then it will not be imported
        then it will not be applied when the server is run

        so, to solve this problem you can import any file contains seeder inside the `AppConfig` class of your app
        """

        # import all `seeders.py` files from all installed apps
        for app_config in apps.get_app_configs():
            app_name = app_config.name
            module_name = 'seeders'
            file_name = module_name + '.py'
            file_path = Path(app_config.path) / file_name
            if file_path.exists():
                spec = importlib.util.spec_from_file_location(f"{app_name}.{module_name}", str(file_path))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

        # if it is runserver command without `--dont-seed` arg
        # call the `SeederRegistry.seed_all()` method to apply all the registered seeders
        if 'runserver' in sys.argv and not '--dont-seed' in sys.argv:
            from seeding.seeders import SeederRegistry
            SeederRegistry.seed_all()

        # call the original ready method
        return super().ready()
