from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from . import views as vw
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
#from .models import FormQuestions

urlpatterns = (
    [
        path("help_on_template", TemplateView.as_view(template_name="home.html"), name="home"),
        path("", auth_views.LoginView.as_view(), name="login"),
        path("logout", auth_views.LogoutView.as_view(), name="logout"),
        path("admin/", admin.site.urls, name='admin'),
        path("todo/", include("todo.urls", namespace="todo"), name='todo'),
        path("bg_form/", vw.BgCreate.as_view(), name='BG-Form'),
        url(r'bg_form/(?P<pk>[0-9]+)/$', login_required(vw.BgUpdate.as_view()), name='BG-Update'),
        path("bg_gm/", login_required(vw.BgView.as_view()), name='BG-GM'),
    ]
    # Static media in DEBUG mode:
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
