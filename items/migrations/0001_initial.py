# Generated by Django 4.2.6 on 2023-10-25 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('shopcart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sell_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('shop_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shopcart.shoppingcart')),
            ],
        ),
    ]
