from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout,login,authenticate
from django.views.generic import DetailView
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .models import *

def home(request):

    carousel=Carousel.objects.all()
    blogs=Blog.objects.filter(approved_blog=True).order_by('-rank')[:4]
    books=Book.objects.all().order_by('-shared_date')[:4]
    mpbs=Most_popular_books.objects.all()
    ctgry=Category.objects.all()
    pop_blogs=Course.objects.all().order_by('-rank')[:3]
    return render(request,"home.html",{"books":books,"blogs":blogs,"carousel":carousel,"mpbs":mpbs,"ctgries":ctgry,"courses":pop_blogs})
    

def about(request):

    data=About_part.objects.first()
    return render(request, 'about.html',{"data":data})

# def contact(request):
#     if request.method=="POST":
#         send_mail(
#             request.POST.get("firstname"),
#             request.POST.get("subject"),
#             request.POST.get("e-mail"),
#             ['elvinc402@gmail.com'],
#             fail_silently=False,
#         )
#         return redirect("/")
#     contact=ContactPart.objects.first()
#     return render(request, 'contact.html',{"contact":contact})


def courses(request):

    book_all=Course.objects.all().order_by('-created_date')
    blogs=Course.objects.all().order_by('created_date')[:4]
    return render(request,"courses.html",{"blogs":blogs,"posts":book_all})

@login_required
def courses_detail(request,id):

    data=Course.objects.filter(id=id).first()
    if data:
        return render(request,'courses_detail.html',{"blg":data})
    else :
        raise  Http404("<h1>Page not found</h1>")



def search(request):

    query = request.GET.get('q')
    if query:
        data=Blog.objects.filter(title__icontains=query,approved_blog=True).order_by('-created_date')
    else:
        data=[]
    posts_all=Blog.objects.filter(approved_blog=True).order_by('-created_date')[:4]
    return render(request,"blogs.html",{"data":data,"blogs":posts_all,"posts":data})
 


def blogs(request):

    posts_all=Blog.objects.filter(approved_blog=True).order_by('-created_date')
    blogs=Blog.objects.filter(approved_blog=True).order_by('-created_date')[:4]
    return render(request,"blogs.html",{"blogs":blogs,"posts":posts_all})



def books_list(request):

    book_all=Book.objects.all().order_by('-shared_date')
    blogs=Blog.objects.filter(approved_blog=True).order_by('-created_date')[:4]
    return render(request,"books.html",{"blogs":blogs,"posts":book_all})



@login_required
def create(request):

    form=BLogForm()
    if request.method=='POST':
        data=request.POST
        if data:
            form=BLogForm(request.POST, request.FILES)
            if form.is_valid():

                data=form.save(commit=False)
                data.author=request.user
                data.save()
                return redirect("/")
    return render(request,"create.html",{"form":form})


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('/')

    else:
        form = SignUpForm()
    return render (request,'signup.html',{'form':form})


def Login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect("/")
        
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

@login_required
def Logout(request):

    logout(request)
    return redirect('/') 



# def description(request, id):
#     blog = blogs.objects.get(id=id)
#     print(blog.title)
#     nom=Nominatim()
   
    # comments = Comment.objects.filter(post=id)
    # if request.method == "POST":
    #     post = get_object_or_404(Blog, id=id)
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.post = post
    #         comment.save()
    #         return redirect('blog_detail', id=post.id)
    # else:
    #     form = CommentForm()
#     blogs = Blog.objects.filter(blog=id)
#     print(blogs)


def Detailview(request,id):

    data=Blog.objects.filter(id=id,approved_blog=True).first()
    say=data.countview
    say+=1
    Blog.objects.filter(id=id,approved_blog=True).update(countview=say)
    comments = Comment.objects.filter(post=id)
    form=CommentForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            post = get_object_or_404(Blog, id=id)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('blog_details', id=post.id)
        else:
            return redirect("/login")
    else:
        form = CommentForm()
   
    if data:
        return render(request,'single.html',{"blg":data,"form":form,"comments":comments,'say':say})
    else :
        raise  Http404("<h1>Page not found</h1>")


def BookDetail(request,id):

    data=Book.objects.filter(id=id).first()

    if data:
        return render(request,'book_detail.html',{"blg":data})
    else :
        raise  Http404("<h1>Page not found</h1>")


def category(request,name):

    blogs=Blog.objects.filter(approved_blog=True).order_by('-created_date')[:4]

    posts=Blog.objects.filter(tag__name=name,approved_blog=True).order_by('-created_date')
    print(posts)
    return render(request,'category.html',{"blogs":blogs,"posts":posts,"tag":name})




    
@login_required
def voting(request,id):

    ranking=Blog.objects.filter(id=id,approved_blog=True).first().rank
    ranking+=int(request.POST.get("voting"))
    Blog.objects.filter(id=id,approved_blog=True).update(rank=ranking)
    return redirect("/blogs/"+str(id))
    

@login_required
def course_voting(request,id):

    ranking=Course.objects.filter(id=id).first().rank
    ranking+=int(request.POST.get("voting"))
    Course.objects.filter(id=id).update(rank=ranking)
    return redirect("/courses/"+str(id))


@login_required
def user_prfile(request,id):

    user=User.objects.filter(id=id).first()
    if user==request.user:
        if request.method=="POST":
            User.objects.filter(id=id).delete()
            return redirect("/")
        blog=Blog.objects.filter(author=request.user,approved_blog=True).order_by("-created_date")
        return render(request,"user_profile.html",{'blogs':blog})
    else:
        return user_prfile(request,request.user.id)
    





def book_category(request,category):

    name=category
    blogs=Book.objects.all().order_by('shared_date')[:4]

    posts=Book.objects.filter(tag__name=name).order_by('-shared_date')
    return render(request,'book_category.html',{"blogs":blogs,"posts":posts,"tag":name})



def course_category(request,category):

    name=category
    blogs=Course.objects.all().order_by('created_date')[:4]
    posts=Course.objects.filter(tag__name=name).order_by('-created_date')
    return render(request,'course_category.html',{"blogs":blogs,"posts":posts,"tag":name})

