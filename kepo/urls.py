"""kepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from kepo_app.views import IndexView, InfoPtnView, EditArticleView, AddArticleView, AdminLoginView, ArticleView, MerchView, AboutView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('info_ptn/', InfoPtnView.as_view(), name="info_ptn"),
    path('article/<slug:article_slug>/edit/', EditArticleView.as_view(), name="edit_article"),
    path('add_article/', AddArticleView.as_view(), name="add_article"),
    path('admin_login/', AdminLoginView.as_view(), name="admin_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('about/', AboutView.as_view(), name="about"),
    path('article/<slug:article_slug>', ArticleView.as_view(), name="article"),
    path('merch/', MerchView.as_view(), name="merch"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
