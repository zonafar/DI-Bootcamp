from django.shortcuts import render, redirect
from contacts.models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    nom = request.POST['nom']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    annonce = request.POST.get('annonce')
    user_id = request.POST['user_id']
    annonce_id = request.POST['annonce_id']
    agent_email = request.POST['agent_email']
    # Verifier si l'utilisateur à déjà postuler
    if request.user.is_authenticated:
        user_id =  request.user.id
        has_contacted = Contact.objects.all().filter(annonce_id = annonce_id, user_id = user_id)
        if has_contacted:
            messages.error(request, 'Vous avez déjà postuler à cette annonce')
            return redirect("annonce",annonce_id)
    contact = Contact(
        annonce = annonce,
        annonce_id = annonce_id,
        nom = nom,
        email = email,
        phone = phone,
        message = message,
        user_id = user_id,
    )

    contact.save()

    subject = 'Demande sur une annonce'
    message = f"Il y'a une demande sur l'annonce [ {annonce} ], Connectez-vous sur votre compte pour en savoir plus."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [agent_email, 'gafarzongo@gmail.com']
    send_mail( subject, message, email_from, recipient_list, fail_silently = False )


    messages.success(request, 'Votre demande a bien été soumis')
    return redirect("annonce",annonce_id)


def detail_contact(request,id):
    contact = Contact.objects.get(pk = id)
    return render(request,'accounts/dashboard/contact.html', {'contact':contact})