# Generated by Django 4.1.7 on 2023-03-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "holon",
            "0020_rename_connection_contract_type_connectioncontract_connectioncontracttype_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="heatgridnode",
            name="type",
            field=models.CharField(
                choices=[("MT", "Mt"), ("HT", "Ht"), ("LT", "Lt")], max_length=2
            ),
        ),
    ]
