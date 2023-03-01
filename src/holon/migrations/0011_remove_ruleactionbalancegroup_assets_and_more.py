# Generated by Django 4.1.7 on 2023-03-01 11:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("holon", "0010_merge_20230301_1216"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ruleactionbalancegroup",
            name="assets",
        ),
        migrations.AddField(
            model_name="ruleactionbalancegroup",
            name="asset_order",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(blank=True, max_length=255), size=None
                ),
                default=[],
                size=None,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ruleactionbalancegroup",
            name="selected_asset",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
