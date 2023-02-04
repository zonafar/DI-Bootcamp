# from django.shortcuts import render,redirect,get_object_or_404
# from location.models import *
# from location.forms import *


# # Create your views here.

# def propriete_get_all(requests):
#     proprietes = Propriete.objects.all()
#     context = {'proprietes':proprietes}
#     return render(requests,'locations/resultats.html',context)

# def propriete_get(requests,pk):
#     propriete = Propriete.objects.get(id = pk)
#     context = {'propriete':propriete}
#     return render(requests,'locations/propriete.html',context)


# def propriete_add(request):
#     if request.method == "GET":
#         form = ProprieteForm()
#     if request.method == 'POST':
#         form = ProprieteForm(request.POST)
#         if form.is_valid():
#             p = form.save()
#         return redirect('location.propriete_get', p.id)
#     return render(request, 'locations/propriete_create.html', {'form':form})
        

# def propriete_edit(request,pk=None):
#     post = get_object_or_404(Propriete, pk=pk)
#     if request.method == "POST":
#         form = ProprieteForm(request.POST,
#                         instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('location.propriete_get_all')
#     else:
#         form = ProprieteForm(instance=post)

#     return render(request,
#                   'locations/propriete_edit.html',
#                   {
#                       'form': form,
#                       'post': post
#                   })


# def propriete_delete(request, pk=None):
#     propriete = get_object_or_404(Propriete, pk=pk)
#     if request.method == "POST":
#         form = ProprieteDeleteForm(request.POST,
#                               instance=propriete)
#         if form.is_valid():
#             propriete.delete()
#             return redirect('post_create')
#     else:
#         form = ProprieteDeleteForm(instance=propriete)
#     return render(request, 'locations/propriete_delete.html',
#                   {
#                       'form': form,
#                       'post': propriete,
#                   })



from django.shortcuts import render,redirect,get_object_or_404
from location.models import *
from location.forms import *
from django.views import generic
from django.urls import reverse_lazy
from annonces.choices import ville_choices,prix_choices,chambre_choices

# class HomeView(generic.ListView):
#     template_name = 'accueil.html'
#     context_object_name = 'proprietes'
#     def get_queryset(self):
#         return Propriete.objects.all() 

# class CreateView(generic.CreateView):
#     model = Propriete
#     template_name = 'propriete/addPropriete.html'
#     form_class =  ProprieteForm

#     def form_valid(self, form):
#         new = form.cleaned_data
#         print(new)
#         return super().form_valid(form)


# class ProprieteUpdateView(generic.UpdateView):
#     model = Propriete
#     template_name = 'propriete/addPropriete.html'
#     form_class =  ProprieteForm

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Propriete, id=id_)

#     def form_valid(self, form):
#         new_film = form.cleaned_data
#         print(new_film)
#         return super().form_valid(form)


 
# class DeleteView(generic.edit.DeleteView):
#     # specify the model you want to use
#     model = Propriete
#     success_url = reverse_lazy('home')

#     template_name = "propriete/propriete_confirm_delete.html"

     

def index(request):
    annonces = Annonce.objects.order_by('-date_annonce').filter(is_published=True)[:3]
    context = {
        'annonces':annonces,

        'ville_choices':ville_choices,
        'prix_choices':prix_choices,
        'chambre_choices':chambre_choices,
    }
    return render(request, '../globalhtml/home.html',context)

def about(request):
    return render(request, '../globalhtml/about.html')