# Generated by Django 4.2 on 2024-03-28 16:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_remove_tag_user_tag_username"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tag",
            new_name="SearchData",
        ),
        migrations.RenameField(
            model_name="searchdata",
            old_name="tag",
            new_name="products",
        ),
    ]
