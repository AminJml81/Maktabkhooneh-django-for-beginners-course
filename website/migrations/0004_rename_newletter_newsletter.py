# Generated by Django 4.2.13 on 2024-06-08 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_newletter"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NewLetter",
            new_name="NewsLetter",
        ),
    ]
