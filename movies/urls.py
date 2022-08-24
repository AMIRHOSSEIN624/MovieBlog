from django.urls import path
from .views import ListMovie, detail_page,comment_like,comment_dislike,category_filter, search_bar

urlpatterns = [
    path('', ListMovie.as_view(), name='home'),
    path('<int:pk>/detail/', detail_page, name='detail_page'),
    path('<int:pk>/detail/like-comment/', comment_like, name='comment_like'),
    path('<int:pk>/detail/dislike-comment/', comment_dislike, name='comment_dislike'),
    path('<int:pk>/genre/', category_filter, name='category'),
    path('serach/', search_bar, name='search'),

]
