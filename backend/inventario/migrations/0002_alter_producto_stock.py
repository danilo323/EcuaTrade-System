import inventario.validators # <--- SIN "backend.."
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(
                default=0, 
                validators=[inventario.validators.validar_stock_producto] # <--- LIMPIO
            ),
        ),
    ]