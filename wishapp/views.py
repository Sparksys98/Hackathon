from django.shortcuts import render,redirect
from .models import WishModel
from .forms import RegisterForm, SigninForm, WishesForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("landing")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)

                return redirect('landing')

    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect('landing')

def landing(request):
    if not request.user.is_authenticated:
        return render(request, 'landing.html')
        #--------------------------------------------------------------------------------------------------------------
    else:
         return render(request,'list.html')
def list(request):
        if request.user.is_authenticated:
            #wishes_url = WishModel.objects.get(pk=pk)
            wishes = WishModel.objects.filter(person=request.user).order_by('-created_date')
            context = {
            "wishes": wishes,
            #"wishes_url": wishes_url
            }
            return render(request, 'list.html', context)
        else:
            return redirect('signin')

def list_create(request):
	if request.user.is_anonymous:
		messages.error(request, "Please sign in to create a new class")
		return redirect('signin')
	form = WishesForm()
	if request.method == "POST":
		form = WishesForm(request.POST, request.FILES)
		if form.is_valid():
			wish = form.save(commit=False)
			wish.person = request.user
			wish.save()
			messages.success(request, "Wish Successfully Created!")
			return redirect('list')
	context = {
		"form": form,
	}
	return render(request, 'createlist.html', context)

# def list_delete(request, wish_id):
#     if request.user.is_authenticated:
#         WishModel.objects.get(id=wish_id).delete()
#         return redirect('list')
#     else:
#         return redirect('signin')

def list_delete(request, wish_id):
    if request.user.is_authenticated:
        user = request.user
        WishModel.objects.filter(id=wish_id).delete()
        return redirect('list')
    elif request.user.is_anonymous:
        return redirect('signin')
