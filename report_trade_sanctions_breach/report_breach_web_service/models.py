# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_type = models.ForeignKey("CompanyType", models.DO_NOTHING)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "company"
        db_table_comment = "{semantic:companies}"


class CompanyNonUk(models.Model):
    company = models.OneToOneField(Company, models.DO_NOTHING, primary_key=True)
    website = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    address_4 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    postcode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "company_non_uk"
        db_table_comment = "Needs to create an empty  address line with one character. Otherwise contact in sql becomes null\n{semantic:companies}"


class CompanyRole(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = "company_role"
        db_table_comment = "the role in the breach. \n{semantic:companies}"


class CompanyType(models.Model):
    id = models.IntegerField(primary_key=True)
    short_label = models.CharField(max_length=20)
    long_label = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = "company_type"
        db_table_comment = "the type indicating whether a company is in company house, uk companies not in company house,  non uk companies.\n{semantic:companies}"


class CompanyUkCh(models.Model):
    company = models.OneToOneField(Company, models.DO_NOTHING, primary_key=True)
    registered_number = models.CharField(
        max_length=10,
        db_comment="This length may not match CH number. However, it needs to be checked with ICMS and LITE.",
    )

    class Meta:
        managed = False
        db_table = "company_uk_ch"
        db_table_comment = "UK limited company in Companies House"


class CompanyUkNonCh(models.Model):
    company = models.OneToOneField(Company, models.DO_NOTHING, primary_key=True)
    website = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = "company_uk_non_ch"


class Content(models.Model):
    question = models.OneToOneField(
        "Question", models.DO_NOTHING, primary_key=True
    )  # The composite primary key (question_id, report_id) found, that is not supported. The first column is selected.
    report = models.ForeignKey("Report", models.DO_NOTHING)
    creation_date = models.DateField()
    json_answer = models.TextField()  # This field type is a guess.
    schema_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "content"
        unique_together = (("question", "report"),)
        db_table_comment = "answers to questions for a report."


class Document(models.Model):
    report = models.OneToOneField(
        "Report", models.DO_NOTHING, primary_key=True
    )  # The composite primary key (report_id, ref, creation_date) found, that is not supported. The first column is selected.
    ref = models.IntegerField()
    creation_date = models.DateField()
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "document"
        unique_together = (("report", "ref", "creation_date"),)
        db_table_comment = "Stores the path to documents stored securely."


class JsonSchema(models.Model):
    id = models.IntegerField(primary_key=True)
    schema = models.TextField()
    label = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "json_schema"


class OtherRegime(models.Model):
    regime = models.OneToOneField(
        "Regime", models.DO_NOTHING, primary_key=True
    )  # The composite primary key (regime_id, report_id) found, that is not supported. The first column is selected.
    description = models.CharField(max_length=100)
    report = models.ForeignKey("Report", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "other_regime"
        unique_together = (("regime", "report"),)
        db_table_comment = "stores other regime typed by the users"


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    json_question = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    schema_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "question"
        db_table_comment = "questions asked to the reporters.  We use JSON to model the answers. It is simplifies the answers and model. "


class Regime(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(
        unique=True,
        max_length=20,
        db_comment="Legal short name used for analytical purposes for grouping.",
    )
    full_name = models.CharField(
        unique=True,
        max_length=100,
        db_comment="Regime label shown on the front end to support user interaction. ",
    )
    start_date = models.DateField(db_comment="start of the legislation application.")
    end_date = models.DateField(db_comment="date the legislation stop its application")
    shown_gui_flag = models.BooleanField(
        db_comment="boolean flag indicating whether the regime shown to the users. "
    )

    class Meta:
        managed = False
        db_table = "regime"
        db_table_comment = "List of regime and countries under trading sanctions.  This table refers to legislation with a start and end date. "


class Relationship(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    shown_gui_flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = "relationship"
        db_table_comment = "the reporter relationship to the company"


class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    creation_date = models.DateField()
    regime = models.ForeignKey(Regime, models.DO_NOTHING)
    type = models.ForeignKey("ReportType", models.DO_NOTHING)
    unique_ref = models.CharField(max_length=6)
    start_breach_date = models.DateField(blank=True, null=True)
    end_breach_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "report"


class ReportCompany(models.Model):
    report = models.OneToOneField(
        Report, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (report_id, company_id, company_role_id) found, that is not supported. The first column is selected.
    company = models.ForeignKey(Company, models.DO_NOTHING)
    company_role = models.ForeignKey(CompanyRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "report_company"
        unique_together = (("report", "company", "company_role"),)


class ReportReporter(models.Model):
    report = models.OneToOneField(
        Report, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (report_id, reporter_id, relationship_id) found, that is not supported. The first column is selected.
    reporter = models.ForeignKey("Reporter", models.DO_NOTHING)
    relationship = models.ForeignKey(Relationship, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "report_reporter"
        unique_together = (("report", "reporter", "relationship"),)
        db_table_comment = (
            "created a many to many relationship for future proofing and avoid duplication of data."
        )


class ReportType(models.Model):
    id = models.IntegerField(primary_key=True)
    short_label = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = "report_type"


class Reporter(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(
        max_length=50, db_comment="The length is not relevant.  it is fine to make it longer. "
    )
    email = models.CharField(max_length=50, db_comment="increase the length as you wish.")
    email_verified = models.BooleanField()

    class Meta:
        managed = False
        db_table = "reporter"
        db_table_comment = "the person who report the breach"


class VerificationCode(models.Model):
    reporter = models.OneToOneField(
        Reporter, models.DO_NOTHING, primary_key=True
    )  # The composite primary key (reporter_id, creation_date_time) found, that is not supported. The first column is selected.
    creation_date_time = models.DateField()
    expiry_date_time = models.DateField()
    succesful_verification_date = models.DateField()
    code = models.CharField(
        max_length=6,
        db_comment="This code is generated randomly. The length can vary from the one used here for testing.",
    )

    class Meta:
        managed = False
        db_table = "verification_code"
        unique_together = (("reporter", "creation_date_time"),)
        db_table_comment = "contains generated code with successful verification. "


# This model is a WIP while we are awaiting the final schema
# class BreachDetails(models.Model):
#     # might not be needed, as django can auto create a primary key
#     report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     reporter_full_name = models.CharField(null=False)
#     reporter_email_address = models.EmailField(null=False)
#     reporter_professional_relationship = models.TextField(null=False)

# class Report
# class Org
# class
