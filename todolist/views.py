from django.shortcuts import redirect, render
from .models import list
from .forms import listForm
from django.contrib import messages

def home(request):

    if request.method == 'POST':
        form= listForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request , ("item add to list !"))
            all_items= list.objects.all
            return render(request, 'home.html' , {'all_items': all_items})

    else:
        all_items= list.objects.all
        return render(request, 'home.html' , {'all_items': all_items})
        

    
def about(request):
    return render(request, 'about.html' , {})


def delete(request , list_id):
    item= list.objects.get(pk=list_id)
    item.delete()

    return redirect('home')
    

def cross_off(request , list_id):
    item= list.objects.get(pk=list_id)
    if item.completed == False:
        item.completed = True
        item.save()
    else:
        item.completed = False
        item.save()

    return redirect('home')


def edit(request , list_id):
    

    if request.method == 'POST':
        item= list.objects.get(pk=list_id)
        form= listForm(request.POST or None , instance= item)

        if form.is_valid():
            item.save()
            return redirect('home')
    else:
        item= list.objects.get(pk=list_id)
        return render(request, 'edit.html' , {'item': item})

    

    
