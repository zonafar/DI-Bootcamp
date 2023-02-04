from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import registerForm
from django.contrib.auth.forms import AuthenticationForm  # add this
from contacts.models import Contact
from location.models import Annonce
# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Inscription réussi.")
            return redirect("login")
        messages.error(
            request, "Inscription non réussi. Information invalide.")
    form = registerForm()
    return render(request=request, template_name="accounts/register.html", context={"form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Vous êtes connectez en tant que {username}.")
				return redirect("dashboard")
			else:
				messages.error(request, "Paramètres de connexion invalides.")
		else:
			messages.error(request, "Paramètres de connexion invalides.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "Vous êtes maintenant deconnecté.") 
	return redirect("index")


def dashboard(request):
	if request.user.is_authenticated:
		contacts = Contact.objects.all().order_by('-date_contact').filter(user_id=request.user.id)
	context = {
		"contacts":contacts
	}
	return render(request=request, template_name="accounts/dashboard/dashboard.html", context=context)

    # annonce = models.CharField(max_length=200)
    # annonce_id = models.IntegerField()
    # nom = models.CharField(max_length=200)
    # email = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # message = models.TextField()
    # date_contact = models.DateTimeField(default=datetime.now,blank = True)
    # user_id = models.IntegerField(blank=True)