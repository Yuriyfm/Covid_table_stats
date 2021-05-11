from django.apps import AppConfig
# в этом файле содеражтся настройки для данного приложения.

class CovidDatasetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'covid_dataset'
