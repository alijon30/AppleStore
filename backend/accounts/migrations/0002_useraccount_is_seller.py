# Generated by Django 4.2.11 on 2024-03-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="is_seller",
            field=models.BooleanField(default=False),
        ),
    ]
