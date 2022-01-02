from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from bookmark.models import Bookmark

# 함수형 뷰
# def index(request):
#     return render(request, 'bookmark/bookmark_list.html')

# 클래스형 뷰(제네릭 뷰)
class BookmarkListView(ListView):
    # 북마크 목록
    model = Bookmark

class BookmarkCreateView(CreateView):
    # 북마크 등록
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    #bookmark_form 대신에 bookmark_create로 변경
    success_url = reverse_lazy('bookmark:list')
    #페이지 이동 - redirect와 같음

class BookmarkDetailView(DetailView):
    # 북마크 상세 페이지
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    # 북마크 수정
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    # 북마크 삭제
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

