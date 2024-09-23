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
    Name of the figure. This is a character field with a maximum length of 100 characters.
    """

    description = models.TextField()
    """
    A text field to store a detailed description of the figure.
    """

    def __str__(self):
        """
        String representation of the Figure object. This method returns the 
        name of the figure when the object is printed or referenced.
        """
        return self.name
