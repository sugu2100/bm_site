from django.urls import path
from bookmark import views
from bookmark.views import BookmarkListView, BookmarkCreateView, \
    BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    #path('', views.index, name='index')
    # 북마크 목록
    path('', BookmarkListView.as_view(), name='list'),
    # 북마크 등록
    path('create/', BookmarkCreateView.as_view(), name='create'),
    # 북마크 상세
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    # 북마크 수정
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    # 북마크 삭제
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]
