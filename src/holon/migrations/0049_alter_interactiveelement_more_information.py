# Generated by Django 4.1.9 on 2023-06-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("holon", "0048_alter_buildinggridconnection_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interactiveelement",
            name="more_information",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
