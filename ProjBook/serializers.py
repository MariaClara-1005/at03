from decimal import Decimal
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    price_in_dollars = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price', 'pages', 'price_in_dollars']

    def get_price_in_dollars(self, obj):
        # Converte o preço de reais para dólares (taxa fictícia de 5 reais por dólar)
        conversion_rate = Decimal('5.0')  # Use Decimal para garantir precisão
        return obj.price / conversion_rate  # Agora ambos são do tipo Decimal

    # Adicionando a validação para garantir que o título seja único
    def validate_title(self, value):
        if Book.objects.filter(title=value).exists():
            raise serializers.ValidationError(f"Já existe um livro com o título '{value}'.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que 0.")
        return value

    def validate_pages(self, value):
        if value <= 0:
            raise serializers.ValidationError("O número de páginas deve ser positivo.")
        return value
