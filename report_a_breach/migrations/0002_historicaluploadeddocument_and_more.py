# Generated by Django 4.2.9 on 2024-02-05 16:41

import uuid

import django.db.models.deletion
import django_countries.fields
import simple_history.models
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("report_a_breach", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalUploadedDocument",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                ("file", models.TextField(max_length=100)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "breach",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="report_a_breach.breach",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical uploaded document",
                "verbose_name_plural": "historical uploaded documents",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalSanctionsRegimeBreachThrough",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "breach",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="report_a_breach.breach",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sanctions_regime",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="report_a_breach.sanctionsregime",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical sanctions regime breach through",
                "verbose_name_plural": "historical sanctions regime breach throughs",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalSanctionsRegime",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                ("short_name", models.TextField()),
                ("full_name", models.TextField()),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical sanctions regime",
                "verbose_name_plural": "historical sanctions regimes",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalPersonOrCompany",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "person_or_company",
                    models.CharField(
                        choices=[("person", "Person"), ("company", "Company")], max_length=7
                    ),
                ),
                ("name", models.TextField()),
                ("website", models.URLField(null=True)),
                ("address_line_1", models.TextField()),
                ("address_line_2", models.TextField(null=True)),
                ("address_line_3", models.TextField(null=True)),
                ("address_line_4", models.TextField(null=True)),
                ("town_or_city", models.TextField()),
                ("county", django_countries.fields.CountryField(max_length=2)),
                ("postcode", models.TextField()),
                (
                    "type_of_relationship",
                    models.CharField(
                        choices=[
                            ("breacher", "Breacher"),
                            ("supplier", "Supplier"),
                            ("recipient", "Recipient"),
                        ],
                        max_length=9,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "breach",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="report_a_breach.breach",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical person or company",
                "verbose_name_plural": "historical person or companys",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalBreach",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "reporter_professional_relationship",
                    models.TextField(
                        choices=[
                            (
                                "owner",
                                "I'm an owner, officer or employee of the company, or I am the person",
                            ),
                            (
                                "acting",
                                "I do not work for the company, but I'm acting on their behalf to make a voluntary declaration",
                            ),
                            (
                                "third_party",
                                "I work for a third party with a legal responsibility to make a mandatory declaration",
                            ),
                            (
                                "no_professional_relationship",
                                "I do not have a professional relationship with the company or person or I no longer have a professional relationship with them",
                            ),
                        ],
                        verbose_name="What is the professional relationship with the company or person suspected of breaching sanctions?",
                    ),
                ),
                (
                    "reporter_email_address",
                    models.EmailField(max_length=254, verbose_name="What is your email address?"),
                ),
                ("reporter_full_name", models.TextField(verbose_name="What is your full name?")),
                (
                    "additional_information",
                    models.TextField(verbose_name="Tell us about the suspected breach"),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical breach",
                "verbose_name_plural": "historical breachs",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]