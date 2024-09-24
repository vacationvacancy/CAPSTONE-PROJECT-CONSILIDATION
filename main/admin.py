from django.contrib import admin
from .models import Figure

@admin.register(Figure)
class FigureAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Figure objects in the Django admin panel.

    This class customizes the display and search functionality for Figure
    models in the admin interface. Figures will be displayed in a list with 
    their name and description, and the search bar allows for filtering based 
    on the name field.
    """

    list_display = ('name', 'description')
    """
    Fields to display in the list view of the Figure model in the admin panel.

    :type: tuple
    :value: ('name', 'description')

    Displays the 'name' and 'description' of each Figure instance.
    """
    
    search_fields = ('name',)
    """
    Fields that will be used in the search bar in the admin panel.

    :type: tuple
    :value: ('name',)
    
    Allows admins to search Figure instances by their 'name'.
    """
