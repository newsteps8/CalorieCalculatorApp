from django.shortcuts import render, HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Busra',
        }
    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'home.html', context)

def contact_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Busra',
        }
    else:
        context = {
            'isim': 'Misafir Kullanıcı'
        }
    return render(request, 'contact.html', context)