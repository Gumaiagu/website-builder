from django.shortcuts import render
from django.conf import settings
from os import path

from .models import Site, Link

# Create your views here.
def page(request, site_name):
    site = Site.objects.get(nome=site_name)

    name = site.nome
    description = site.descricao
    icon = site.icone.url

    text_color = site.cor_de_texto
    background_color = site.cor_de_fundo

    x = site.twitter_x
    instagram = site.instagram
    facebook = site.facebook

    other_links = Link.objects.filter(site=site)

    info = {
        'name': name,
        'description': description,
        'icon': icon,

        'text_color': text_color,
        'background_color': background_color,

        'x': x,
        'instagram': instagram,
        'facebook': facebook,
        'links': other_links,
        }
    
    return render(request, 'site_template/index.html', info)
