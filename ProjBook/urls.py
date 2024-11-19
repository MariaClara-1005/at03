from django.urls import path
from .views import BookListView, create_book

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', create_book, name='book-create'),  # Novo endpoint POST
]
