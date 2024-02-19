from django.urls import reverse
from django.views.generic import FormView
from formtools.wizard.views import NamedUrlSessionWizardView


class BaseView(FormView):
    template_name = "form.html"


class BaseModelFormView(BaseView):
    def __init__(self):
        super().__init__()

    def form_valid(self, form):
        breach_instance = form.save(commit=False)
        session_data = self.request.session.get("breach_instance", {})
        if "id" not in session_data.keys():
            session_data["id"] = str(breach_instance.id)
        form_data = form.cleaned_data
        session_data.update({key: value for key, value in form_data.items()})
        self.request.session["breach_instance"] = session_data
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            self.success_path, kwargs={"pk": self.request.session["breach_instance"]["id"]}
        )


class BaseWizardView(NamedUrlSessionWizardView):
    def get_template_names(self):
        if custom_getter := getattr(self, f"get_{self.steps.current}_template_name", None):
            return custom_getter()
        return super().get_template_names()

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if custom_getter := getattr(self, f"get_{self.steps.current}_context_data", None):
            context.update(custom_getter(form))
        return context

    def process_step(self, form):
        if custom_getter := getattr(self, f"process_{self.steps.current}_step", None):
            return custom_getter(form)
        return super().process_step(form)

    def post(self, request, **kwargs):
        # TODO: this code isn't reachable if the user selects change on the summary page.
        # TODO: need further debug - possible to add to a process step
        # TODO: investigate wizard forms redirect methods?
        for key, value in request.POST.items():
            print(key, value)
            if value == "summary":
                kwargs["redirect_to"] = "summary"
                print(kwargs)
                return super().post(request, **kwargs)
        for key, value in kwargs.items():
            print(f"kwargs {key, value}")
            if key == "redirect_to":
                print("attempting redirect to summary page")
                return reverse("summary")
        return super().post(request, **kwargs)
