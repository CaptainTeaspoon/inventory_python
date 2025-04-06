from django.shortcuts import render
from .models import Items, Usergroups, Users, Warehouse

# Create your views here.

def kontrolluebersicht(request):
    items = Items.objects.all()
    user_groups = Usergroups.objects.all()
    users = Users.objects.all()
    warehouses = Warehouse.objects.all()

    context = {
        'items': items,
        'user_groups': user_groups,
        'users': users,
        'warehouses': warehouses,
    }
    return render(request, 'kontrolluebersicht.html', context)