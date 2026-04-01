# Create your views here.
from django.shortcuts import render, redirect
from .models import Producto
from django.core.exceptions import ValidationError

def registrar_producto_view(request):
    if request.method == "POST":
        # 1. Recibimos los datos (esto reemplaza tus parámetros de función)
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock', 0)

        try:
            # 2. Creamos el objeto (Esto reemplaza tu user_data y el Repository)
            nuevo_producto = Producto(
                nombre_producto=nombre.strip().title(),
                precio=precio,
                stock=stock
            )
            
            # 3. ¡IMPORTANTE! Forzamos a Django a revisar tus validadores
            nuevo_producto.full_clean() 
            
            # 4. Guardamos (Esto reemplaza a Fnc_Guardar_producto_db)
            nuevo_producto.save()
            
            mensaje = f"✅ Éxito: El producto {nombre} ya está en la tienda."
            return render(request, 'inventario/registro.html', {'mensaje': mensaje})

        except ValidationError as e:
            # Si algo falla (precio <= 0, nombre vacío), el Model lanza el error aquí
            error_mensaje = f"❌ Error: {e.messages[0]}"
            return render(request, 'inventario/registro.html', {'error': error_mensaje})

    return render(request, 'inventario/registrar.html')


