from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Button
from crispy_forms_gds.layout import Layout
from crispy_forms_gds.layout import Size
from django import forms
from django.utils.safestring import mark_safe

from .constants import PROFESSIONAL_RELATIONSHIP_CHOICES
from .models import JsonSchema
from .models import Question
from .models import Report
from .models import Reporter


class StartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Button("start now", "Start now"))

    # define the report type in the associated view, use the Report pk to build subsequent urls
    class Meta:
        model = Report
        fields = ["type"]


class BaseQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["json_question", "schema_id"]

    def __init__(self, question_label, fields, *args, **kwargs):
        super(BaseQuestionForm).__init__(*args, **kwargs)
        # TODO: might need to overhaul forms and query in the view
        # not sure if the schema id is needed for the query
        questions = Question.json_question.all()
        for question in questions:
            if question == question_label:
                self.question = question
        self.helper = FormHelper()
        self.helper.label_size = Size.MEDIUM
        self.helper.layout = Layout(question_label, Button("continue", "Continue"))


class NameForm(BaseQuestionForm):
    def __init__(self, *args, **kwargs):
        super().__init__("full_name", *args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_size = Size.MEDIUM
        self.helper.layout = Layout("full_name", Button("continue", "Continue"))

        # TODO: once querying the questions are sorted, need to enforce the required field
        full_name = forms.CharField(
            label=mark_safe(f"<strong>{self.question}</strong>"),
            error_messages={"required": "Please enter your name as it appears on your passport"},
            widget=forms.TextInput(attrs={"id": "full_user_name"}),
        )

    class Meta:
        model = Reporter
        fields = ["full_name"]


# class EmailForm(forms.ModelForm):
#     email = forms.EmailField(
#         label=mark_safe("<strong>What is your email address</strong>"),
#         error_messages={"required": "We need to send you an email to verify your email address"},
#         widget=forms.TextInput(attrs={"id": "reporter_email_address"}),
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.label_size = Size.MEDIUM
#         self.helper.layout = Layout("email", Button("continue", "Continue"))
#
#     class Meta:
#         model = Reporter
#         fields = ["email"]
#
#
# class EmailVerifyForm(forms.ModelForm):
#     reporter_verify_email = forms.CharField(
#         label=mark_safe("<strong>We've sent you an email</strong>"),
#         help_text="Enter the 6 digit security code",
#         error_messages={"required": "Please enter the 6 digit security code provided in the email"},
#         widget=forms.TextInput(attrs={"id": "reporter_verify_email"}),
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.label_size = Size.MEDIUM
#         self.helper.layout = Layout("reporter_verify_email", Button("continue", "Continue"))
#
#     # class Meta:
#     #     model = BreachDetails
#     #     exclude = [
#     #         "reporter_full_name",
#     #         "reporter_email_address",
#     #         "reporter_professional_relationship",
#     #     ]
#
#
# class ProfessionalRelationshipForm(forms.ModelForm):
#     reporter_professional_relationship = forms.ChoiceField(
#         choices=((choice, choice) for choice in PROFESSIONAL_RELATIONSHIP_CHOICES),
#         widget=forms.RadioSelect,
#         label=mark_safe(
#             "<strong>What is the professional relationship with the company or person suspected of breaching "
#             "sanctions?</strong>"
#         ),
#         error_messages={"required": "Please select one of the choices to continue"},
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         # TODO: check why this helper isn't working
#         self.helper.label_size = Size.MEDIUM
#         self.helper.layout = Layout(
#             "reporter_professional_relationship", Button("continue", "Continue")
#         )
#
#     # class Meta:
#     #     model = BreachDetails
#     #     fields = ["reporter_professional_relationship"]
#
#
# class SummaryForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(Button("submit", "Submit"))
#
#     # class Meta:
#     #     model = BreachDetails
#     #     exclude = [
#     #         "reporter_email_address",
#     #         "reporter_full_name",
#     #         "reporter_professional_relationship",
#     #     ]
