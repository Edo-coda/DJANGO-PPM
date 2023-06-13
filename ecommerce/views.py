from django.shortcuts import render, redirect, reverse
from .models import Product, User, Order
from django.contrib.auth import authenticate, login
# Create your views here.

def ecommerce(request):
    lista=[]
    request.session['prodotto']= lista
    request.session['costo'] = lista
    request.session['pconf'] = lista
    request.session['numero'] = 0
    request.session['totale'] = 0
    products = Product.objects.all()
    return render(request, 'ecommerce/ecommerce.html', {'products':products})

def accesso(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    return render(request, 'ecommerce/accesso.html', {'products':products})

def search(request):
    query_dict = request.GET
    query = query_dict.get("query")
    product_s=None
    for product in Product.objects.all():
        if product.nome == query:
            product_s = product
    context = {
        "object": product_s
    }
    return render(request, 'ecommerce/search.html', context=context)

def registrati(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        cognome = request.POST.get("cognome")
        email = request.POST.get("email")
        pw = request.POST.get("pw")
        for u in User.objects.all():
            if (u.email == email):
                context = {
                    "error": "Utente già registrato, esegui accesso"
                }
                return render(request, 'ecommerce/registrati.html', context)
        user_object = User.objects.create(nome=nome, cognome=cognome, email=email, password=pw)
        return redirect('/home/accedi')
    return render(request, 'ecommerce/registrati.html', {})

def accedi(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pw = request.POST.get("pw")
        products = Product.objects.all()
        user = None
        for u in User.objects.all():
            if(u.email == email and u.password == pw):
                user = u
        if user is None:
            context = {
                "error": "Email o Password errate, riprova"
            }
            return render(request, 'ecommerce/accedi.html', context)
        request.session['user'] = user.nome
        request.session['email'] = user.email
        return redirect('accesso')
    return render(request, 'ecommerce/accedi.html', {})

def sport(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/sport.html',  {'products':products})

def giocattoli(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/giocattoli.html',  {'products':products})

def elettrodomestici(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/elettrodomestici.html',  {'products':products})

def libri(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/libri.html',  {'products':products})

def ordini(request):
    orders = Order.objects.all()
    user = request.session['email']
    ordini = []
    prodotti = []
    for o in orders:
        if o.utente.email == user:
            ordini.append(o)
    return render(request, 'ecommerce/ordini.html',  {'orders':ordini})

def carrello(request):
    products = Product.objects.all()
    if request.method == "POST":
        costi = request.session['costo']
        prodotti = request.session['prodotto']
        pconf = request.session['pconf']
        costo = 0
        for p in prodotti:
            if 'elimina' in request.POST:
                if p == request.POST.get('elimina'):
                    prodotti.remove(p)
            else:
                if request.POST.get(p) != None:
                    quantità = int(request.POST.get(p))
                    for pr in products:
                        if pr.nome == p:
                            costo = round(quantità*pr.prezzo, 2)
                            costi.append(costo)
                    prodotti.remove(p)
                    pconf.append(p)
        request.session['prodotto'] = prodotti
        request.session['costo'] = costi
        request.session['pconf'] = pconf
        return redirect('ordine')
    return render(request, 'ecommerce/carrello.html',  {'products':products})

def sport_a(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    return render(request, 'ecommerce/sport_a.html',  {'products':products})

def giocattoli_a(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    return render(request, 'ecommerce/giocattoli_a.html',  {'products':products})

def elettrodomestici_a(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    return render(request, 'ecommerce/elettrodomestici_a.html',  {'products':products})

def libri_a(request):
    products = Product.objects.all()
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    return render(request, 'ecommerce/libri_a.html',  {'products':products})

def search_a(request):
    if request.method == "POST":
        prodotto = request.POST.get("pr_nome")
        prodotti = request.session['prodotto']
        prodotti.append(prodotto)
        request.session['prodotto']=prodotti
        return redirect('carrello')
    query_dict = request.GET
    query = query_dict.get("query")
    product_s=None
    for product in Product.objects.all():
        if product.nome == query:
            product_s = product
    context = {
        "object": product_s
    }
    return render(request, 'ecommerce/search_a.html', context=context)

def ordine(request):
    prodotti = request.session['pconf']
    costi = request.session['costo']
    pc = {}
    numero = 0
    i = 0
    for o in Order.objects.all():
        numero = o.numero
    numero += 1
    totale = 0
    for c in costi:
        totale += c

    totale = round(totale,2)

    for p in prodotti:
        pc[p] = costi[i]
        i+=1

    request.session['numero'] = numero
    request.session['totale'] = totale
    return render(request, 'ecommerce/ordine.html', {'pc': pc, 'numero':numero, 'totale':totale})

def elimina(request):
    lista = []
    request.session['prodotto']= lista
    request.session['costo'] = lista
    request.session['pconf'] = lista
    return render(request, 'ecommerce/elimina.html', {})

def conferma(request):
    numero = request.session['numero']
    totale = request.session['totale']
    costi = request.session['costo']
    products = Product.objects.all()
    users = User.objects.all()
    user = request.session['email']
    utente = None
    prodotti = []
    disp = 0
    i=0
    for p in request.session['pconf']:
        for pr in products:
            if p == pr.nome:
                prodotti.append(pr)
                disp = pr.disponibilità
                quantita = costi[i]/pr.prezzo
                disp -= quantita
                pr.disponibilità = disp
                pr.save()
        i+=1
    for u in users:
        if u.email == user:
            utente = u
    order_object = Order.objects.create(numero=numero, utente=utente, totale=totale)
    for prod in prodotti:
        order_object.prodotti.add(prod)
    lista = []
    request.session['prodotto']= lista
    request.session['costo'] = lista
    request.session['pconf'] = lista
    request.session['numero'] = 0
    request.session['totale'] = 0
    return render(request, 'ecommerce/conferma.html', {})
