from django.shortcuts import render
from django.views import View
from kepo_app.forms import ArticleForm
from kepo_app.models import Article, Category

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class InfoPtnView(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'info_ptn.html', {'form': form})
    
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
        return render(request, 'infoptn_edit.html', {})