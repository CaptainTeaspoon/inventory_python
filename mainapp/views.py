from django.shortcuts import render, redirect, get_object_or_404        
from .models import Items, Usergroups, Users, Warehouse
from .forms import ItemForm, UsergroupForm, UserForm, WarehouseForm, LoginForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def landing_page(request):
    user_group = request.user.userprofile.Usergroup  # Assuming a OneToOne relation in your User model
    warehouses = Warehouse.objects.filter(usergroup=user_group)
    items = Items.objects.filter(warehouse__usergroup=user_group)
    context = {'warehouses': warehouses, 'items': items}
    return render(request, 'landing_page.html', context)


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

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.Warehouse.Usergroup = request.user.user.Usergroup  # Assign usergroup from logged-in user
            item.save()
            messages.success(request, 'Artikel erfolgreich erstellt!')
            return redirect('landing_page')
    else:
        form = ItemForm()
    # Limit Warehouse choices in the form based on user's group
    form.fields['Warehouse'].queryset = Warehouse.objects.filter(Usergroup=request.user.user.Usergroup)
    return render(request, 'item_create.html', {'form': form})

@login_required
def warehouse_create(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.Usergroup = request.user.user.Usergroup
            warehouse.save()
            messages.success(request, 'Lager erfolgreich erstellt!')
            return redirect('warehouse_list')
    else:
        form = WarehouseForm()
        # Limit Usergroup choices if needed (usually admin only)
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

@login_required
def item_update(request, pk):
    item = get_object_or_404(Items, pk=pk, Warehouse__Usergroup=request.user.user.Usergroup)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully')
            return redirect('landing_page')
    else:
        form = ItemForm(instance=item)
        # Limit Warehouse choices in the form based on user's group (optional)
        form.fields['Warehouse'].queryset = Warehouse.objects.filter(Usergroup=request.user.user.Usergroup)
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

@login_required
def warehouse_update(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk, Usergroup=request.user.user.Usergroup)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lager erfolgreich aktualisiert!')
            return redirect('warehouse_list')
    else:
        form = WarehouseForm(instance=warehouse)
        # Limit Usergroup choices if needed (usually admin only)
    return render(request, 'warehouse_update.html', {'form': form, 'warehouse': warehouse})

#Delete

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Items, pk=pk, Warehouse__Usergroup=request.user.user.Usergroup)
    item.delete()
    messages.success(request, 'Article deleted successfully')
    return redirect('landing_page')

def user_delete(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('landing_page')
    return render(request, 'user_delete_confirm.html', {'user': user})

def user_group_delete(request, pk):
    user_group = get_object_or_404(Usergroups, pk=pk)
    if request.method == 'POST':
        user_group.delete()
        messages.success(request, 'Usergroup deleted successfully')
        return redirect('landing_page')
    return render(request, 'usergroup_delete_confirm.html', {'usergroup': user_group})

def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('landing_page')
    return render(request, 'warehouse_delete_confirm.html', {'user': warehouse})


@login_required
def warehouse_list(request):
    user_group = request.user.user.Usergroup
    warehouses = Warehouse.objects.filter(Usergroup=user_group)
    return render(request, 'warehouse_list.html', {'warehouses': warehouses})

@login_required
def item_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        user_group = request.user.user.Usergroup
        results = Items.objects.filter(Q(Name__icontains=query) | Q(Barcode__icontains=query), Warehouse__Usergroup=user_group)
    return render(request, 'item_search_results.html', {'results': results, 'query': query})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try custom authentication
            user = authenticate(request, username=name, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                form.add_error(None, 'Ungültiger Benutzername oder Passwort.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})