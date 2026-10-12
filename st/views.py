from django.shortcuts import render
import datetime
def m(request):
    name='Tirth'
    now=datetime.datetime.now()
    return render(request,'about.html',{'name':name,'now':now})