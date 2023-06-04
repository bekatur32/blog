from django.urls import path
from .views import PostListView, post_detail, post_share, post_comment, post_list, post_search

app_name = 'blog' 

urlpatterns = [
   # path('', PostListView.as_view(), name='post_list'),
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', post_list,name='post_id_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share,name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('search/',post_search, name='post_search')
]
