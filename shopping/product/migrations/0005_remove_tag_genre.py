# Generated by Django 4.2 on 2024-03-28 15:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_remove_tag_person_name_tag_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="genre",
        ),
    ]
