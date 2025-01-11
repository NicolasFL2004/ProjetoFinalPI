from django.apps import AppConfig


class GameinsightConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gameinsight'

    def ready(self):
        import gameinsight.signals
