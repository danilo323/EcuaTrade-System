from rest_framework import viewsets, permissions
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from .permissions import IsOwnerOrReadOnly

# Nueva vista para que React pueda leer las categorías del Mega Menú
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Optimizamos: Traemos las categorías e imágenes de un solo golpe (más rápido)
        queryset = Producto.objects.all().select_related('categoria').prefetch_related('imagenes', 'variantes')
        
        # Si estamos en el panel de ADMIN de la API y queremos ver solo lo nuestro:
        # Pero para la TIENDA (frontend), siempre devolvemos todo para que el cliente vea los productos.
        return queryset

    def perform_create(self, serializer):
        # El "Sello de Propiedad" se mantiene intacto
        serializer.save(vendedor=self.request.user)