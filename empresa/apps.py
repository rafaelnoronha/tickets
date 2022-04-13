from django.apps import AppConfig


class EmpresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empresa'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import empresa.signals