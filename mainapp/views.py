from django.shortcuts import render, redirect, get_object_or_404        
from .models import Items, Usergroups, Users, Warehouse
from .forms import ItemForm, UsergroupForm, UserForm, WarehouseForm
from django.contrib import messages

# Create your views here.

#Create

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

#Update

def item_update(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item) # 'instance' bindet das Formular an das existierende Objekt
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('kontrolluebersicht')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_update.html', {'form': form, 'item': item})

def user_update(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully')
            return redirect('kontrolluebersicht')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_update.html', {'form': form, 'user': user})

def user_group_update(request, pk):
    user_group = get_object_or_404(Usergroups, pk=pk)
    if request.method == 'POST':
        form = UsergroupForm(request.POST, instance=user_group)
        if form.is_valid():
            form.save()
            messages.success(request, 'User group updated successfully')
            return redirect('kontrolluebersicht')
    else:
        form = UsergroupForm(instance=user_group)
    return render(request, 'usergroup_update.html', {'form': form, 'user_group': user_group})

def warehouse_update(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Warehouse updated successfully')
            return redirect('kontrolluebersicht')
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouse_update.html', {'form': form, 'warehouse': warehouse})