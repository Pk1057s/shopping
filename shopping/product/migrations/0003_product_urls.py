# Generated by Django 4.2 on 2024-03-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_product_tag_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="urls",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]