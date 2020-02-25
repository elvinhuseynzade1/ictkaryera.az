from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Blog,Category,Book_category,Course_category,
				Carousel,Course,Comment,
				Most_popular_books,Book,About_part])

