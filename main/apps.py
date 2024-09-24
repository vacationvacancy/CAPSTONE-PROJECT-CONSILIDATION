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
    for models in this app.

    :type: str
    """

    name = 'main'

    """
    The name of the Django application.

    :type: str
    """
