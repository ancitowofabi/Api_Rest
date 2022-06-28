from django.urls import path, include
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("somos/", views.somos, name="somos"),
    path("galeria/", views.galeria, name="galeria"),
    path("contacto/", views.contacto, name="contacto"),
    path("register/", views.register, name="register"),
    path("imc/", views.imc, name="imc"),
    path("inspirate/", views.inspirate, name="inspirate"),
    path("login/", views.login, name="login"),
    path("form_crear_item/", views.form_crear_item, name="form_crear_item"),
    path("form_mod_item/<id>", views.form_mod_item, name="form_mod_item"),
    path("form_del_item/<id>", views.form_del_item, name="form_del_item"),
    path("mostrar_item/", views.mostrar_item, name="mostrar_item"),
    path("mostrar_cliente/", views.mostrar_cliente, name="mostrar_cliente"),
    path("form_crear_cliente/", views.form_crear_cliente, name="form_crear_cliente"),
    path("form_mod_cliente/<id>", views.form_mod_cliente, name="form_mod_cliente"),
    path("form_del_cliente/<id>", views.form_del_cliente, name="form_del_cliente"),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

