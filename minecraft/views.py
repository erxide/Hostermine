from django.shortcuts import render, redirect
from .forms import serverForm
from accounts.models import CustomUser
from minecraft.models import server
from .GestionServer import gestionserver

# Create your views here.

def create_server(request):
    if request.user.have_server:
        return redirect('/')
    if request.method == 'POST':
        form = serverForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(id=request.user.id)
            server_instance = form.save(commit=False)
            user.have_server = True
            server_instance.save()
            user.server = server_instance
            user.save()
            gestionserver.create_server(request.user, server_instance)
            gestionserver.modify_server_properties(request.user, server_instance)
            gestionserver.create_docker_compose(request.user, server_instance)
            gestionserver.run_docker(request.user)
            return redirect('/')
    else :
        form = serverForm()
    return render(request, 'minecraft/create_server.html', {'form':form})

def modify_server(request):
    if not request.user.have_server:
        return redirect('/minecraft/createserver')
    serv = server.objects.get(id=request.user.server.id)
    if request.method == 'POST':
            form = serverForm(request.POST, instance=serv)
            if form.is_valid():
                form.save()
                gestionserver.modify_server_properties(request.user, serv)
                gestionserver.reload_docker(request.user)
                return redirect('/')
    else :
        form = serverForm(instance=serv)
    return render(request, 'minecraft/modifyserver.html', {'form':form})


def sup_server(request):
    user = CustomUser.objects.get(id=request.user.id)
    serv = server.objects.get(id=user.server.id)
    gestionserver.sup_server(request.user)
    user.have_server = False
    user.server = None
    user.save()
    serv.delete()
    gestionserver.sup_docker(request.user)
    return redirect('/')

def test_request(request):
    res = gestionserver.sup_docker(request.user)
    return render(request, 'minecraft/test.html', {'resultat':res})