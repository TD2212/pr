from django.shortcuts import redirect, render, get_object_or_404
from .models import student
import datetime
from .forms import forms,STUDENTFORM
def home(request):
    return render(request,'home.html',)

def student_list(request):
    students = student.objects.all()
    return render(request, 'cruds/list.html', {'student': students})




def st_add(request):
    if request.method == 'POST':
        forms = STUDENTFORM(request.POST)

        if forms.is_valid():
            name = forms.cleaned_data['S_name']
            email = forms.cleaned_data['S_email']
            mobile = forms.cleaned_data['S_mobile']
            city = forms.cleaned_data['S_city']

            student.objects.create(
                S_name=name,
                S_email=email,
                S_mobile=mobile,
                S_city=city
            )

            return redirect('list')
    else:
        forms = STUDENTFORM()

    return render(request, 'cruds/add.html', {'forms': forms})

def st_delete(request, id):
    s = get_object_or_404(student, S_id=id)

    if request.method == 'POST':
        s.delete()
        return redirect('list')

    return render(request, 'cruds/delete.html', {'s': s})

def st_update(request, id):
    s = get_object_or_404(student, S_id=id)

    if request.method == 'POST':
        form = STUDENTFORM(request.POST, instance=s)

        if form.is_valid():
            form.save()
            return redirect('list')

    else:
        form = STUDENTFORM(instance=s)

    return render(request, 'cruds/update.html', {'form': form})