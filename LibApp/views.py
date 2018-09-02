from django.shortcuts import render
from .models import Student, Book, IssuedBook, Librarian
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
def librarian(request):
	if request.method == 'POST':
		bid=request.POST['bookId']
#get librarian id also 
		lib=request.POST['lil']
		obj = IssuedBook.objects.filter(bookId = bid).filter(current_status = True)
		delta = datetime.now().date() - obj.returned_date
		if delta < 0:
			obj.returned_date=datetime.now().date()
			obj.current_status = False
			obj2=Book.objects.filter(bookId=bid)
			obj2.status=True
			obj.save()
			obj2.save()
#send this back 2 library login page
			return render(request,'lib.html')
		else:
			fine=delta
			return render(request,'libfile.html',{'fine2':fine, 'obj2':obj, 'lid':lib})

def librarianfine(request):
	if request.method == 'POST':
#input type=hidden 
		bid=request.POST['bookId']
		fin=request.POST['fcol']
		lib=request.POST['lil']
		obj = IssuedBook.objects.filter(bookId = bid).filter(current_status = True)
		obj.returned_date=datetime.now().date()
		obj.current_status = False
		obj2 = Book.objects.filter(bookId=bid)
		obj2.status=True
		obj3 = Librarian.objects.filter(libId = lib)
		ob3.fine=ob3.fine+fin
		obj.save()
		obj2.save()
		obj3.save()
#send this back 2 library login page
		return render(request,'lib.html')

def login_it(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username, password=password)

	if user is None:
		return render(request,'/account/login.html',{'error':'Invlid username/password'})
	else:
		login(request,user)
		if(Librarian.objects.filter(user=user).count>0):
			lbu=Librarian.objects.get(user=user)
			return render(request,'lib.html',{'lbu':lbu})
		else:
			stu=Student.objects.get(user=user)	                                                                 
			return render(request,'stui.html',{'stu':stu})

#def student(request):


