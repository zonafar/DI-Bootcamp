from django.shortcuts import render,get_object_or_404
from location.models import Annonce,Agent
from django.core.paginator import Paginator

# Create your views here.

def annonce(request,id):
    annonce = get_object_or_404(Annonce,pk=id)
    agent = annonce.agent
    context = {
        "annonce" : annonce,
        "agent" : agent
    }
    return render(request, 'annonces/annonce.html',context)


def annonces(request):
    annonces = Annonce.objects.order_by('-date_annonce').filter(is_published=True)

    paginator = Paginator(annonces, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "annonces" : page_obj
    }
    return render(request, 'annonces/annonces.html',context)


def search(request):
    queryset_list = Annonce.objects.order_by('-date_annonce')
    service = ''
    # Keywords
    if 'keywords' in request.GET:
        # print(request.GET['keywords'])
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(ville__icontains=keywords)
            print(queryset_list)

    # Louer Vendre
    if 'inlineRadioOptions' in request.GET:
        radio = request.GET['inlineRadioOptions']
        if radio == 'Louer':
            service = 'louer'
        


    # taille
    if 'taille' in request.GET:
        state = request.GET['taille']
        if state:
            queryset_list = queryset_list.filter(taille__lte=state)
    # categorie
    # if 'categorie' in request.GET:
    #     state = request.GET['categorie']
    #     if state:
    #         queryset_list = queryset_list.filter(state__iexact=state)

    # Prix min
    if 'inputMin' in request.GET:
        prix = request.GET['inputMin']
        if prix:
            queryset_list = queryset_list.filter(prix__gte=prix)

    # Prix max
    if 'inputMax' in request.GET:
        prix = request.GET['inputMax']
        if prix:
            queryset_list = queryset_list.filter(prix__lte=prix)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        # 'state_choices': state_choices,
        # 'bedroom_choices': bedroom_choices,
        # 'price_choices': price_choices,
        'annonces': queryset_list,
        'values': request.GET,
        'service': service,
    }
    # return render(request, 'annonces/search.html')
    return render(request, 'annonces/annonces.html',context)