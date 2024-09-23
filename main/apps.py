from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    Configuration class for the 'main' application in the Django project.

    This class defines the configuration settings for the 'main' app,
    such as the default primary key field type and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    """
    Specifies the type of auto-created primary key field to use by default
    for models in this app. 'BigAutoField' generates a big integer field
    for auto-incremented IDs.
    """

    name = 'main'
    """
    The name of the Django application. This is the Python path to the app's
    configuration module, which is used by Django to identify the app.
    """
