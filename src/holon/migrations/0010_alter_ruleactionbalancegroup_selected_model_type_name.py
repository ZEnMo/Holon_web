# Generated by Django 4.1.7 on 2023-03-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0009_merge_20230314_1644"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ruleactionbalancegroup",
            name="selected_model_type_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
