# Generated by Django 4.2.10 on 2024-03-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report_a_breach", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalpersonorcompany",
            name="reference",
        ),
        migrations.RemoveField(
            model_name="personorcompany",
            name="reference",
        ),
        migrations.AddField(
            model_name="breach",
            name="reference",
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name="Reference"),
        ),
        migrations.AddField(
            model_name="historicalbreach",
            name="reference",
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name="Reference"),
        ),
    ]