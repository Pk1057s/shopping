# Generated by Django 4.2 on 2024-03-28 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0003_product_urls"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="person_name",
        ),
        migrations.AddField(
            model_name="tag",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
