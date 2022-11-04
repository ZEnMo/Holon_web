# Generated by Django 4.1.3 on 2022-11-04 07:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_storylinepageinformationtype_storylinepageroletype_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storylinepageinformationtype",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
        ),
        migrations.AlterField(
            model_name="storylinepageroletype",
            name="slug",
            field=autoslug.fields.AutoSlugField(editable=False, populate_from="name"),
        ),
    ]
