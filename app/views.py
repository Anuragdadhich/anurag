from django.shortcuts import render,HttpResponse
from app.models import contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lsname = request.POST.get('lsname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        index = contact(name=name, lsname=lsname, email=email, mobile=mobile, subject=subject, message=message)
        index.save()
    return render(request,'index.html')
