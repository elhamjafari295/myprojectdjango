from django.contrib.auth import views
from django.urls import path
from .views import ArticleList, ArticleCreate, UpdateView,ArticleUpdate,ArticleDelete,profile



app_name = 'account'

urlpatterns = [
    path('', ArticleList.as_view() , name="home"),
    path('article/create', ArticleCreate.as_view() , name="article-create"),
    path('article/update/<int:pk>', ArticleUpdate.as_view() , name="article-update"),
    path('article/delete/<int:pk>', ArticleDelete.as_view() , name="article-delete"),
    path('profile/', profile.as_view() , name="profile")

]