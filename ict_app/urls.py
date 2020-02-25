
from django.urls import path,re_path
from . import views
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='ict-home'),
    path('about/', views.about, name='ict-about'),
    # path('contact/', views.contact, name='ict-contact'),
    path('blogs/', views.blogs, name='ict-blogs'),
    path('create/', views.create, name='ict-create'),
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('blogs/<int:id>/', views.Detailview,name='blog_details'),
    path('category/<str:name>/', views.category,name='blog_category'),
    path("search/",views.search,name='search'),
    path('voting/<int:id>', views.voting, name='voting'),
    path('books/<int:id>/', views.BookDetail,name='book_details'),
    path('books/', views.books_list, name='ict-books_list'),
    path('courses/', views.courses, name='ict-courses'),
    path('courses/<int:id>', views.courses_detail, name='ict-courses_detail'),
    path('course_voting/<int:id>', views.course_voting, name='course_voting'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("profile/<int:id>",views.user_prfile),


    path("book/<str:category>/",views.book_category,name='book_category'),
    path("course/<str:category>/",views.course_category,name='course_category'),
    
]



