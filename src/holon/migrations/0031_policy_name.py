# Generated by Django 4.1.7 on 2023-04-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0030_alter_contract_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="policy",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
