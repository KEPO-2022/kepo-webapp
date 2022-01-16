from django.shortcuts import render
from django.views import View
from kepo_app.forms import ArticleForm
from kepo_app.models import Article, Category
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

class InfoPtnView(View):
    def get(self, request):
        ctx = {}
        article_list_konten_edukatif = Article.objects.filter(category__name='Konten Edukatif')
        article_list_jalur_masuk_ptn = Article.objects.filter(category__name='Jalur Masuk PTN')
        article_list_video_jurusan = Article.objects.filter(category__name='Video Jurusan')
        # article_list = Article.objects.get()
        ctx['konten_edukatif'] = article_list_konten_edukatif
        ctx['jalur_masuk_ptn'] = article_list_jalur_masuk_ptn
        ctx['video_jurusan'] = article_list_video_jurusan
        return render(request, 'infoptn.html', ctx)
    
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

class AddArticleView(View):
    @method_decorator(staff_member_required(redirect_field_name='', login_url='index'))
    def get(self, request):
        form = ArticleForm()
        category_list = Category.objects.all()
        return render(request, 'infoptn_edit.html', {'form': form, 'category_list': category_list})
    
    @method_decorator(staff_member_required(redirect_field_name='', login_url='index'))
    def post(self, request):
        id = request.POST.get('cat')
        try:
            category = Category.objects.get(id=int(id))
        except:
            category= None
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            if category:
                article = form.save(commit=False)
                article.category = category
                article.save()
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('add_article'))

class EditArticleView(View):
    @method_decorator(staff_member_required(redirect_field_name='', login_url='index'))
    def get(self, request, article_slug):
        ctx = {}
        try:
            if request.GET['delarticle_id']:
                article_id = request.GET['delarticle_id']
                article = Article.objects.get(id=article_id)
                article.delete()
                ctx_dict = {}
                return HttpResponseRedirect(reverse('info_ptn'))
        except: 
            pass
        try:
            article = Article.objects.get(slug=article_slug)
            ctx['article'] = article
        except Article.DoesNotExist:
            ctx['article'] = None
        form = ArticleForm()
        category_list = Category.objects.all()
        ctx['form'] = form
        ctx['category_list'] = category_list
        return render(request, 'edit_article.html', context=ctx)

    @method_decorator(staff_member_required(redirect_field_name='', login_url='index'))
    def post(self, request, article_slug):
        id = request.POST.get('cat')
        try:
            category = Category.objects.get(id=int(id))
        except:
            category= None
        article = Article.objects.get(slug=article_slug)
        form = ArticleForm(request.POST, request.FILES, instance=article)
        is_thumbnail = request.FILES.get('thumbnail')
        thumbnail = article.thumbnail
        if form.is_valid() and is_thumbnail != None:
            if category:
                article = form.save(commit=False)
                article.category = category
                article.save()
        elif is_thumbnail == None:
            article = form.save(commit=False)
            article.category = category
            article.thumbnail = thumbnail
            article.save()
            print(article.thumbnail)
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse('edit_article', args=(article_slug,)))

class ArticleView(View):
    def get(self, request, article_slug):
        ctx = {}
        try:
            article = Article.objects.get(slug=article_slug)
            ctx['article'] = article
        except Article.DoesNotExist:
            ctx['article'] = None
        return render(request, 'article.html', context=ctx)
        
class MerchView(View):
    def get(self, request):
        return render(request, 'merch.html', {})

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html', {})

    def post(self, request):
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'admin_login.html', {})
        else:
            return render(request, 'admin_login.html', {})

class LogoutView(View):
    @method_decorator(staff_member_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})