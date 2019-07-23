from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import borrowbook, retuenbook
from .models import BorrowBooks

# Create your views here.

def index(request):
    return render(request, 'index.html')

def borrow(request):
    if request.method == 'GET':
        print('get*********')
        form = borrowbook()
        return render(request, 'Book/borrow.html', {'form':form})
    else:
        print('post*********')
        form = borrowbook(request.POST)
        if form.is_valid():
            b1_name = request.POST.get('b_name')
            stu1_id = request.POST.get('stu_id')
            stu1_name = request.POST.get('stu_name')
            stu1_phone = request.POST.get('stu_phone')
            stu1_qq = request.POST.get('stu_qq')
            BorrowBooks.objects.create(b_name = b1_name, stu_id = stu1_id, stu_name = stu1_name,
                                       stu_phone=stu1_phone, stu_qq=stu1_qq)
            return render(request, 'index.html', {"flag":"3"})
        else:
            return render(request, 'Book/borrow.html')

def returning(request):
    if request.method == 'GET':
        print('get*********')
        form = retuenbook()
        return render(request, 'Book/returning.html', {'form':form})
    else:
        print('post*********')
        form = retuenbook(request.POST)
        if form.is_valid():
            b1_name = request.POST.get('b_name')
            stu1_id = request.POST.get('stu_id')
            delte = BorrowBooks.objects.filter(stu_id=stu1_id).filter(b_name__contains=b1_name)
            if len(delte) > 0:
                for i in delte:
                    i.delete()
                return render(request, 'index.html', {"flag": "1"})
            else:
                return render(request, 'Book/returning.html', {'form':form, "flag":"2"})
        else:
            return render(request, 'Book/returning.html')

def success(request):
    return render(request, 'Book/success.html')