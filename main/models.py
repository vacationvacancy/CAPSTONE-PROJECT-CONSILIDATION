from django.db import models


class Figure(models.Model):

    """
    Model representing a figure entity.

    This model stores information about figures, including their name and 
    description. It can be used for managing data related to figures in the 
    application.
    """

    name = models.CharField(max_length=100)

    """
    Name of the figure.

    :type: str
    """

    description = models.TextField()

    """
    A detailed description of the figure.

    :type: str
    """

    def __str__(self):

        """
        String representation of the Figure object.

        :return: The name of the figure.
        :rtype: str
        """
        
        return self.name
