# Generated by Django 4.2.11 on 2024-03-13 16:12

from django.conf import settings
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import django_chunk_upload_handlers.clam_av
import django_countries.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sessions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Breach",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "reporter_professional_relationship",
                    models.TextField(
                        choices=[
                            ("owner", "I'm an owner, officer or employee of the business, or I am the person"),
                            (
                                "acting",
                                "I do not work for the business or person, but I'm acting on their behalf to make a voluntary declaration",
                            ),
                            (
                                "third_party",
                                "I work for a third party with a legal responsibility to make a mandatory declaration",
                            ),
                            (
                                "no_professional_relationship",
                                "I do not have a professional relationship with the business or person, or I no longer have a professional relationship with them",
                            ),
                        ]
                    ),
                ),
                ("reporter_email_address", models.EmailField(max_length=254)),
                ("reference", models.CharField(blank=True, max_length=6, null=True)),
                ("reporter_full_name", models.CharField(max_length=255)),
                (
                    "reporter_name_of_business_you_work_for",
                    models.CharField(max_length=300, verbose_name="Business you work for"),
                ),
                ("when_did_you_first_suspect", models.TextField()),
                ("unknown_sanctions_regime", models.BooleanField(blank=True, default=False)),
                ("other_sanctions_regime", models.BooleanField(blank=True, default=False)),
                ("additional_information", models.TextField()),
                ("what_were_the_goods", models.TextField()),
                (
                    "business_registered_on_companies_house",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No"), ("do_not_know", "I do not know")], max_length=11),
                ),
                (
                    "do_you_know_the_registered_company_number",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No")], max_length=3),
                ),
                ("registered_company_number", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "were_there_other_addresses_in_the_supply_chain",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No"), ("do_not_know", "I do not know")], max_length=11),
                ),
                ("other_addresses_in_the_supply_chain", models.TextField(blank=True, null=True)),
                ("tell_us_about_the_suspected_breach", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SanctionsRegime",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("short_name", models.TextField()),
                ("full_name", models.TextField()),
                ("date_range", django.contrib.postgres.fields.ranges.DateRangeField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UploadedDocument",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "file",
                    models.FileField(upload_to="", validators=[django_chunk_upload_handlers.clam_av.validate_virus_check_result]),
                ),
                ("breach", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="report_a_breach.breach")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SanctionsRegimeBreachThrough",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("breach", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="report_a_breach.breach")),
                (
                    "sanctions_regime",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="report_a_breach.sanctionsregime"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ReporterEmailVerification",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("email_verification_code", models.CharField(max_length=6)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("reporter_session", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sessions.session")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PersonOrCompany",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("person_or_company", models.CharField(choices=[("person", "Person"), ("company", "Company")], max_length=7)),
                ("name", models.TextField()),
                ("website", models.URLField(blank=True, null=True)),
                ("address_line_1", models.TextField()),
                ("address_line_2", models.TextField(blank=True, null=True)),
                ("address_line_3", models.TextField(blank=True, null=True)),
                ("address_line_4", models.TextField(blank=True, null=True)),
                ("town_or_city", models.TextField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("county", models.TextField(blank=True, null=True)),
                ("postal_code", models.TextField()),
                (
                    "type_of_relationship",
                    models.CharField(
                        choices=[("breacher", "Breacher"), ("supplier", "Supplier"), ("recipient", "Recipient")], max_length=9
                    ),
                ),
                ("breach", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="report_a_breach.breach")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalUploadedDocument",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "file",
                    models.TextField(
                        max_length=100, validators=[django_chunk_upload_handlers.clam_av.validate_virus_check_result]
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
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
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
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
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
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
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
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
                ("date_range", django.contrib.postgres.fields.ranges.DateRangeField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
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
            name="HistoricalReporterEmailVerification",
            fields=[
                ("id", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("modified_at", models.DateTimeField(blank=True, editable=False)),
                ("email_verification_code", models.CharField(max_length=6)),
                ("date_created", models.DateTimeField(blank=True, editable=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "reporter_session",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sessions.session",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical reporter email verification",
                "verbose_name_plural": "historical reporter email verifications",
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
                ("person_or_company", models.CharField(choices=[("person", "Person"), ("company", "Company")], max_length=7)),
                ("name", models.TextField()),
                ("website", models.URLField(blank=True, null=True)),
                ("address_line_1", models.TextField()),
                ("address_line_2", models.TextField(blank=True, null=True)),
                ("address_line_3", models.TextField(blank=True, null=True)),
                ("address_line_4", models.TextField(blank=True, null=True)),
                ("town_or_city", models.TextField()),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("county", models.TextField(blank=True, null=True)),
                ("postal_code", models.TextField()),
                (
                    "type_of_relationship",
                    models.CharField(
                        choices=[("breacher", "Breacher"), ("supplier", "Supplier"), ("recipient", "Recipient")], max_length=9
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
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
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
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
                            ("owner", "I'm an owner, officer or employee of the business, or I am the person"),
                            (
                                "acting",
                                "I do not work for the business or person, but I'm acting on their behalf to make a voluntary declaration",
                            ),
                            (
                                "third_party",
                                "I work for a third party with a legal responsibility to make a mandatory declaration",
                            ),
                            (
                                "no_professional_relationship",
                                "I do not have a professional relationship with the business or person, or I no longer have a professional relationship with them",
                            ),
                        ]
                    ),
                ),
                ("reporter_email_address", models.EmailField(max_length=254)),
                ("reference", models.CharField(blank=True, max_length=6, null=True)),
                ("reporter_full_name", models.CharField(max_length=255)),
                (
                    "reporter_name_of_business_you_work_for",
                    models.CharField(max_length=300, verbose_name="Business you work for"),
                ),
                ("when_did_you_first_suspect", models.TextField()),
                ("unknown_sanctions_regime", models.BooleanField(blank=True, default=False)),
                ("other_sanctions_regime", models.BooleanField(blank=True, default=False)),
                ("additional_information", models.TextField()),
                ("what_were_the_goods", models.TextField()),
                (
                    "business_registered_on_companies_house",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No"), ("do_not_know", "I do not know")], max_length=11),
                ),
                (
                    "do_you_know_the_registered_company_number",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No")], max_length=3),
                ),
                ("registered_company_number", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "were_there_other_addresses_in_the_supply_chain",
                    models.CharField(choices=[("yes", "Yes"), ("no", "No"), ("do_not_know", "I do not know")], max_length=11),
                ),
                ("other_addresses_in_the_supply_chain", models.TextField(blank=True, null=True)),
                ("tell_us_about_the_suspected_breach", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                ("history_type", models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1)),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "reporter_email_verification",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="report_a_breach.reporteremailverification",
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
        migrations.AddField(
            model_name="breach",
            name="reporter_email_verification",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="report_a_breach.reporteremailverification"
            ),
        ),
        migrations.AddField(
            model_name="breach",
            name="sanctions_regimes",
            field=models.ManyToManyField(
                blank=True, through="report_a_breach.SanctionsRegimeBreachThrough", to="report_a_breach.sanctionsregime"
            ),
        ),
    ]
