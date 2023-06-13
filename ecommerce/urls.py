from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecommerce, name='home'),
    path('registrati', views.registrati, name='registrati'),
    path('accedi', views.accedi, name='accedi'),
    path('sport', views.sport, name='sport'),
    path('giocattoli', views.giocattoli, name='giocattoli'),
    path('elettrodomestici', views.elettrodomestici, name='elettrodomestici'),
    path('libri', views.libri, name='libri'),
    path('search', views.search, name='search'),
    path('accesso', views.accesso, name='accesso'),
    path('accesso/ordini', views.ordini, name='ordini'),
    path('accesso/carrello', views.carrello, name='carrello'),
    path('accesso/sport', views.sport_a, name='sport_a'),
    path('accesso/giocattoli', views.giocattoli_a, name='giocattoli_a'),
    path('accesso/elettrodomestici', views.elettrodomestici_a, name='elettrodomestici_a'),
    path('accesso/libri', views.libri_a, name='libri_a'),
    path('accesso/search', views.search_a, name='search_a'),
    path('accesso/ordine', views.ordine, name='ordine'),
    path('accesso/ordine/elimina', views.elimina, name='elimina'),
    path('accesso/ordine/conferma', views.conferma, name='conferma')
]