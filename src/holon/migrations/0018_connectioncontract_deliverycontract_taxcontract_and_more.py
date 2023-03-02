# Generated by Django 4.1.7 on 2023-03-02 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "holon",
            "0017_housegridconnection_pricelevel_high_dif_from_avg_eurpkwh_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ConnectionContract",
            fields=[
                (
                    "contract_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.contract",
                    ),
                ),
                (
                    "connection_contract_type",
                    models.CharField(
                        choices=[("DEFAULT", "Default"), ("NFATO", "Nfato")],
                        max_length=255,
                    ),
                ),
                ("nfATO_capacity_kW", models.FloatField()),
                ("nfATO_starttime_h", models.FloatField()),
                ("nfATO_endtime_h", models.FloatField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.contract",),
        ),
        migrations.CreateModel(
            name="DeliveryContract",
            fields=[
                (
                    "contract_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.contract",
                    ),
                ),
                (
                    "delivery_contract_type",
                    models.CharField(
                        choices=[
                            ("ELECTRICITY_FIXED", "Fixed"),
                            ("ELECTRICITY_VARIABLE", "Variable"),
                        ],
                        max_length=255,
                    ),
                ),
                ("delivery_price_eurpkWh", models.FloatField()),
                ("feedin_price_eurpkWh", models.FloatField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.contract",),
        ),
        migrations.CreateModel(
            name="TaxContract",
            fields=[
                (
                    "contract_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.contract",
                    ),
                ),
                (
                    "tax_contract_type",
                    models.CharField(
                        choices=[
                            ("SALDEREN", "Salderen"),
                            ("NIETSALDEREN", "Nietsalderen"),
                        ],
                        max_length=255,
                    ),
                ),
                ("tax_delivery_eurpkWh", models.FloatField()),
                ("tax_feedin_eurpkWh", models.FloatField()),
                ("proportional_fax_pct", models.FloatField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.contract",),
        ),
        migrations.CreateModel(
            name="TransportContract",
            fields=[
                (
                    "contract_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="holon.contract",
                    ),
                ),
                (
                    "transport_contract_type",
                    models.CharField(
                        choices=[
                            ("DEFAULT", "Default"),
                            ("NODALPRICING", "Nodalpricing"),
                            ("BANDWIDTH", "Bandwidth"),
                        ],
                        max_length=255,
                    ),
                ),
                ("bandwidth_treshold_kW", models.FloatField()),
                ("bandwidth_tariff_eurpkWh", models.FloatField()),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("holon.contract",),
        ),
        migrations.AddField(
            model_name="contract",
            name="annual_fee_eur",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="contract",
            name="energy_carrier",
            field=models.CharField(
                choices=[
                    ("ELECTRICITY", "Electricity"),
                    ("HEAT", "Heat"),
                    ("METHANE", "Methane"),
                    ("HYDROGEN", "Hydrogen"),
                    ("DIESEL", "Diesel"),
                ],
                default="ELECTRICITY",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="type",
            field=models.CharField(
                choices=[
                    ("DELIVERY", "Delivery"),
                    ("TRANSPORT", "Transport"),
                    ("CONNECTION", "Connection"),
                    ("TAX", "Tax"),
                ],
                max_length=255,
            ),
        ),
    ]
