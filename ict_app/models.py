from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Book_category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Course_category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Carousel(models.Model):
    description=models.CharField(max_length=200, blank=True, null=True)
    image=models.ImageField(upload_to='carousel',blank=True)


class Blog(models.Model):
    image=models.ImageField(upload_to="blog_pics",blank=True, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    tag = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    rank=models.IntegerField(default=0)
    countview=models.IntegerField(default=0)
    approved_blog = models.BooleanField(default=False)
    def approve(self):
        self.approved_blog = False
        self.save()
    def __str__(self):
        return self.title
 

class Book(models.Model):
    title = models.CharField(max_length=210)
    image=models.ImageField(upload_to="book_pics",blank=True, null=True)
    shared_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    content=models.TextField(blank=True, null=True)
    file=models.FileField(upload_to="books_file")
    tag = models.ForeignKey(Book_category, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
 

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    post = models.ForeignKey(
        'Blog', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.author.email


class Course(models.Model):
    title=models.CharField(max_length=50,default='add')
    content=models.TextField(default='Nothing')
    course_link=models.TextField(default='Nothing')
    image=models.ImageField( upload_to="course_images",blank=True, null=True)
    rank=models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Course_category, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title


class Most_popular_books(models.Model):
    image=models.ImageField(blank=True, null=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title





class ContactPart(models.Model):
    content=models.TextField()
    number=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return "Yalniz 1 eded olmalidir"




class About_part(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    main_image=models.ImageField()
    second_image=models.ImageField()
    courses=models.PositiveSmallIntegerField()
    books=models.PositiveSmallIntegerField()
    blogs=models.PositiveSmallIntegerField()

    card_title_1=models.CharField(max_length=250)
    card_description_1=models.TextField()

    card_title_2=models.CharField(max_length=250)
    card_description_2=models.TextField() 
    
    card_title_3=models.CharField(max_length=250)
    card_description_3=models.TextField()

    def __str__(self):
        return "Yalniz 1 eded olmalidir"
    






