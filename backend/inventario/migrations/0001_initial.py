import inventario.validators  # <--- LIMPIO
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(
                    max_length=150, 
                    validators=[inventario.validators.validar_nombre_producto] # <--- SIN "backend."
                )),
                ('precio', models.DecimalField(
                    decimal_places=2, 
                    max_digits=10, 
                    validators=[inventario.validators.validar_precio_producto] # <--- SIN "backend."
                )),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]