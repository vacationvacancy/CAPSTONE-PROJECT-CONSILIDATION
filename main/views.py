from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import UserRegistrationForm
from .models import Figure


def home(request):

    """
    View function for the home page.

    Renders the 'home.html' template when users access the home page.

    :param request: The HTTP request object.
    :return: Rendered 'home.html' template.
    """
    
    return render(request, 'main/home.html')


def about(request):

    """
    View function for the about page.

    Renders the 'about.html' template to provide information about the website or application.

    :param request: The HTTP request object.
    :return: Rendered 'about.html' template.
    """

    return render(request, 'main/about.html')


def contact(request):

    """
    View function for the contact page with a user registration form.

    Handles the POST request to register a new user. If the form is valid, the user
    is authenticated and logged in, then redirected to the success page. For GET requests, 
    it displays an empty registration form.
    
    :param request: The HTTP request object.
    :return: Rendered 'contact.html' template with the registration form, or redirect 
             to the 'success' page upon successful registration.
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/contact.html', {'form': form})


def success(request):

    """
    View function for the success page.

    Renders the 'success.html' template after successful user registration or other 
    operations that warrant a success confirmation.

    :param request: The HTTP request object.
    :return: Rendered 'success.html' template.
    """

    return render(request, 'main/success.html')


def figures_view(request):

    """
    View function to display a list of all figures.

    Fetches all the figures from the database and passes them to the 'figures.html' template 
    for rendering.
    
    :param request: The HTTP request object.
    :return: Rendered 'figures.html' template, populated with all figures.
    """

    figures = Figure.objects.all()
    return render(request, 'figures.html', {'figures': figures})
