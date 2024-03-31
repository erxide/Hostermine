from django.shortcuts import render
from minecraft.models import server
from accounts.models import CustomUser

# Create your views here.




def test(request):
    if request.user.is_authenticated:
        serv = CustomUser.objects.get(id=request.user.id).server
        return render(request, 'webserver/index.html', {'serv':serv})
    else:
        return render(request, 'webserver/index.html')