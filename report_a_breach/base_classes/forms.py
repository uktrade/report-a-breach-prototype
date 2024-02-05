from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import Layout
from crispy_forms_gds.layout import Size
from crispy_forms_gds.layout import Submit
from django import forms


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("continue", "Continue", css_class="btn-primary"))
        self.helper.label_size = Size.MEDIUM
        self.helper.layout = Layout(*self.fields)


class BaseModelForm(BaseForm, forms.ModelForm):
    pass
