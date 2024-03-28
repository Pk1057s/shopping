# Generated by Django 4.2 on 2024-03-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_tag_create_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="user",
        ),
        migrations.AddField(
            model_name="tag",
            name="username",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
