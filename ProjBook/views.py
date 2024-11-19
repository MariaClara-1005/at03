from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

# View para criar um novo livro via POST
@api_view(['POST'])
def create_book(request):
    # Checa se a requisição é POST
    if request.method == 'POST':
        # Usa o serializer para validar e salvar os dados
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o novo livro no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna o livro criado com status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erro de validação

# View para listar todos os livros via GET
class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()  # Pega todos os livros
        serializer = BookSerializer(books, many=True)  # Serializa todos os livros
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a lista de livros
