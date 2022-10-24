# Generated by Django 4.1.2 on 2022-10-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_merge_20221021_1317"),
    ]

    operations = [
        migrations.AddField(
            model_name="storylinepage",
            name="description",
            field=models.TextField(
                blank=True, help_text="Description of the storyline", null=True
            ),
        ),
        migrations.AddField(
            model_name="storylinepage",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
