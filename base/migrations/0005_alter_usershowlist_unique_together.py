# Generated by Django 4.1.5 on 2023-07-29 14:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0004_rename_is_favorite_usershowlist_favorite_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="usershowlist",
            unique_together={("user_id", "show_id")},
        ),
    ]
