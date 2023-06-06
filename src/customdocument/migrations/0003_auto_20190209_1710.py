# Generated by Django 2.1.5 on 2019-02-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customdocument", "0002_customdocument_file_size"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customdocument",
            options={"verbose_name": "document", "verbose_name_plural": "documents"},
        ),
        migrations.AddField(
            model_name="customdocument",
            name="file_hash",
            field=models.CharField(blank=True, editable=False, max_length=40),
        ),
    ]
