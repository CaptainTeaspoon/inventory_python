from django.shortcuts import render, redirect
from .models import Items, Usergroups, Users, Warehouse
from .forms import ItemForm, UsergroupForm, UserForm, WarehouseForm
from django.contrib import messages

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

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item created successfully')
            return redirect('kontrolluebersicht') # Redirect zur Übersichtsseite
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def warehouse_create(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Warehouse created successfully')
            return redirect('kontrolluebersicht') # Redirect zur Übersichtsseite
    else:
        form = WarehouseForm()
    return render(request, 'warehouse_create.html', {'form': form})

def user_group_create(request):
    if request.method == 'POST':
        form = UsergroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User group created successfully')
            return redirect('kontrolluebersicht') # Redirect zur Übersichtsseite
    else:
        form = UsergroupForm()
    return render(request, 'usergroup_create.html', {'form': form})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('kontrolluebersicht') # Redirect zur Übersichtsseite
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})
