# Generated by Django 4.1.5 on 2023-07-31 09:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_rename_show_usershowlist_show_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="usershowlist",
            unique_together={("user_id", "show_id")},
        ),
    ]