# Generated by Django 4.1.5 on 2023-07-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="show",
            name="genres",
            field=models.ManyToManyField(blank=True, null=True, to="base.genre"),
        ),
        migrations.AlterField(
            model_name="show",
            name="producers",
            field=models.ManyToManyField(blank=True, null=True, to="base.producer"),
        ),
        migrations.AlterField(
            model_name="show",
            name="studio",
            field=models.ManyToManyField(blank=True, null=True, to="base.studio"),
        ),
        migrations.AlterField(
            model_name="show",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="base.tag"),
        ),
    ]
