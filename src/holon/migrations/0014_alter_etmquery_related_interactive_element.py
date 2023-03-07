# Generated by Django 4.1.6 on 2023-03-06 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("holon", "0013_connectioncontract_cookingconversionasset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etmquery",
            name="related_interactive_element",
            field=models.ForeignKey(
                blank=True,
                help_text="Use this field to relate this query and conversion set to an interactive element (used for rendering in the front-end)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="holon.interactiveelement",
            ),
        ),
    ]
