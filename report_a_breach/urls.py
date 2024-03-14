from django.urls import include, path

urlpatterns = [
    path("", include("report_a_breach.core.urls")),
    path("healthcheck", include("healthcheck.urls")),
]
