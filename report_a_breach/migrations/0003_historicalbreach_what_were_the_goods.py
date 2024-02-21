# Generated by Django 4.2.10 on 2024-02-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report_a_breach", "0002_breach_what_were_the_goods_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalbreach",
            name="what_were_the_goods",
            field=models.TextField(
                default="",
                verbose_name="What were the goods or services, or what was the technological assistance or technology?",
            ),
            preserve_default=False,
        ),
    ]
