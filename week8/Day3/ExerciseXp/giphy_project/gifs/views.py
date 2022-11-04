from django.shortcuts import render,redirect,HttpResponse
from .models import Gif,Category
from .forms import GifForm,CategoryForm
from django.contrib import messages

# Create your views here.

def homepage(request):
    gifs = Gif.objects.all()
    context = {
        'gifs' : gifs
    }
    return render(request,'homepage.html',context)

def add_new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category = form.cleaned_data.get('name')
            print(category)
            messages.success(request, f'New Category created!')
            return redirect('gifs.homepage')
    else:
        form = CategoryForm()
    return render(request,'category.html',{'form':form})

def add_new_gif(request):
    if request.POST:
        form = GifForm(request.POST)
        if form.is_valid():
            gif = form.save(commit=False)
            print(gif)
            gif.save()
            form.save_m2m()
            categories = form.cleaned_data.get('categories')
            print(categories)
            for category in categories:
                gif.categories.add(category)

            messages.success(request, f'New Gif created with success')
            return redirect('gifs.homepage')
    else:
        form = GifForm()
    return render(request,'gifs.html',{"form":form})

def category(request,id):
    c1 = Category.objects.get(id=id)
    context = {
        'gifs':c1.gifs.all()
    }
    return render(request,'category_gifs.html',context)

def gif(request,id):
    c1 = Gif.objects.get(id=id)
    return render(request,'gif.html',{'gif':c1})

def categories(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request,'all_categories.html',context)