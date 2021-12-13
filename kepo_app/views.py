from django.shortcuts import render
from django.views import View
from kepo_app.forms import ArticleForm
from kepo_app.models import Article, Category
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class InfoPtnView(View):
    def get(self, request):
        return render(request, 'infoptn.html', {})
    
    # def post(self, request):
    #     form = CategoryForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('info_ptn'))
    #     else:
    #         print(form.errors)
    #     form = CategoryForm()
    #     cat = Category.objects.all()
    #     return render(request, 'info_ptn.html', {'form': form, 'category_list': cat})

class InfoPtnEdit(View):
    def get(self, request):
        form = ArticleForm()
        category_list = Category.objects.all()
        return render(request, 'infoptn_edit.html', {'form': form, 'category_list': category_list})
    
    def post(self, request):
        id = request.POST.get('cat')
        try:
            category = Category.objects.get(id=int(id))
        except:
            category= None
        form = ArticleForm(request.POST)
        if form.is_valid():
            if category:
                article = form.save(commit=False)
                article.category = category
                article.save()
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('info_ptn_edit'))