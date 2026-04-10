from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializer
from .permissions import IsOwnerOrReadOnly # Tu regla de "Solo el dueño toca"

class ProductoViewSet(viewsets.ModelViewSet):
    # 1. El traductor de datos
    serializer_class = ProductoSerializer

    # 2. Las reglas de seguridad
    # IsAuthenticatedOrReadOnly: Cualquiera ve, logueados crean.
    # IsOwnerOrReadOnly: Solo el dueño del producto puede editar o borrar.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # 3. El filtro inteligente (Lo que me pediste)
    def get_queryset(self):
        user = self.request.user
        
        # Si el usuario es Admin (Staff), ve TODO el inventario
        if user.is_staff:
            return Producto.objects.all()
        
        # Si es un vendedor normal (como Juan), ve SOLO sus productos
        # Si no está logueado, devolvemos todo (para que los clientes puedan comprar)
        if user.is_authenticated:
            return Producto.objects.filter(vendedor=user)
        
        return Producto.objects.all()

    # 4. El "Sello de Propiedad"
    # Cuando se crea un producto, Django le pone el nombre del que está logueado
    def perform_create(self, serializer):
        serializer.save(vendedor=self.request.user)