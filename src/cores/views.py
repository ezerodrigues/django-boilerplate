from django.shortcuts import render
# from utils.cores.factory import make_core



def home(request):
    return render(request, 'cores/pages/home.html', context= {
        })

def cadastro(request):
    return render(request, 'cores/pages/cadastro.html', context= {
        })



