# Generated by Django 4.1.5 on 2023-02-03 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0037_bestpracticeoverviewpage_bestpracticepage_and_more"),
        ("api", "0012_alter_interactiveinputoptions_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="interactiveinput",
            name="link_wiki_page",
            field=models.ForeignKey(
                blank=True,
                help_text="Use this to link to an internal wiki page.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="main.wikipage",
            ),
        ),
        migrations.AddField(
            model_name="interactiveinput",
            name="more_information",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
