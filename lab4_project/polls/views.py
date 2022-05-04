from django.shortcuts import render,redirect
from .forms import CustomerForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            student_id = form.cleaned_data.get('student_id')
            messages.success(request, f' Welcome to website {student_id}')
            return redirect('index')


    context = {'form':form}
    return render(request, 'polls/index.html', context)


def send_message(request):
    email = EmailMessage(
        'Hello',
        'My name is Ayazhan',
        '200103231@stu.sdu.edu.kz',
        ['bakytayazhan2003@gmail.com'],
        headers={'Message-ID':'foo'},
    )

    email.send(fail_silently=False)
    return render(request, 'polls/successfull.html')
