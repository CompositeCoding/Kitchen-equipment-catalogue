from django.shortcuts import render, redirect
from .models import Products
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.generic.edit import FormMixin, FormView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator
from .load_data import load_data

LIJNEN = ['650L','700L','900L','drop']
LIJNENGIORIK = ['Dropin600','60Snackline','FriteusesEnOvens','Salamanders']

def Index(request):
    return render(request, 'Products/Index.html')

class OlisListView(ListView):
    model = Products
    template_name = 'Products/Olis.html'
    def get_context_data(self, **kwargs):
        context = super(OlisListView, self).get_context_data(**kwargs)
        UrlVariable = self.kwargs.get("urlsearch")
        UrLVariableLijn = self.kwargs.get("Lijn")
        for lijn in LIJNEN:
            context[lijn] = sorted(list(set([i.Categorie for i in Products.objects.filter(Bedrijf__contains='Olis').filter(Lijn__contains=lijn[:3])])))
        if UrlVariable:
            queryset = Products.objects.filter(Lijn__contains=UrLVariableLijn)
            queryset2 = Products.objects.filter(Categorie__iexact=UrlVariable)
            context['Cat'] = UrlVariable
            result = queryset.intersection(queryset2)
            context['query'] = result.order_by('-Prijs')
        return context

class GiorikListView(ListView):
    model = Products
    template_name = 'Products/Giorik.html'
    def get_context_data(self, **kwargs):
        context = super(GiorikListView, self).get_context_data(**kwargs)
        UrlVariable = self.kwargs.get("urlsearch")
        UrLVariableLijn = self.kwargs.get("Lijn")
        for lijn in LIJNENGIORIK:
            context[lijn] = sorted(list(set([i.Categorie for i in Products.objects.filter(Lijn__contains=lijn)])))
        if UrlVariable:
            # queryset = Products.objects.filter(Bedrijf__iexact='Olis').filter(Lijn__contains=self.kwargs.get("Lijn"))
            queryset = Products.objects.filter(Lijn__contains=UrLVariableLijn)
            queryset2 = Products.objects.filter(Categorie__iexact=UrlVariable)
            context['Cat'] = UrlVariable
            result = queryset.intersection(queryset2)
            context['query'] = result.order_by('-Prijs')
        return context

def SearchView(request):
    context = dict()

    if 'Apparaat' in request.GET:
        queryset = Products.objects.filter(Typenummer__contains=request.GET.get('Apparaat').upper())
        queryset2 = Products.objects.filter(Categorie__contains=request.GET.get('Apparaat'))
        if len(queryset.union(queryset2)) == 0:
            context['available'] = "This entity was not found in the database"
        else:
            context['query'] = queryset.union(queryset2).order_by('Categorie')
        return render(request, 'Products/Search.html',context)
    return render(request,'Products/Search.html',context)


class OlisProductView(MultipleObjectMixin, FormView):

    model = Products
    template_name = 'Products/Olisproduct.html'
    # form_class = ContactForm
    # success_url = '/Olis/'

    def get_context_data(self, **kwargs):
        context = dict()
        type = self.kwargs.get("typenummer")
        for lijn in LIJNEN:
            context[lijn] = sorted(list(set([i.Categorie for i in Products.objects.filter(Bedrijf__contains='Olis').filter(Lijn__contains=lijn[:3])])))
        if type:
            queryset = Products.objects.filter(Typenummer__iexact=type.upper())
            context['object'] = queryset[0]

        # context['form'] = ContactForm()
        return context

    def form_valid(self, form):
        form.send_email(self.kwargs.get("typenummer"))
        return super().form_valid(form)

class GiorikProductView(MultipleObjectMixin, FormView):

    model = Products
    template_name = 'Products/Giorikproduct.html'
    # form_class = ContactForm
    # success_url = '/Olis/'

    def get_context_data(self, **kwargs):
        context = dict()
        type = self.kwargs.get("typenummer")
        for lijn in LIJNENGIORIK:
            context[lijn] = sorted(list(set([i.Categorie for i in Products.objects.filter(Lijn__contains=lijn)])))
        if type:
            queryset = Products.objects.filter(Typenummer__iexact=type.upper())
            context['object'] = queryset[0]
        # context['form'] = ContactForm()
        return context

    def form_valid(self, form):
        form.send_email(self.kwargs.get("typenummer"))
        return super().form_valid(form)

def load(request):
    load_data()
    return redirect('Index')
