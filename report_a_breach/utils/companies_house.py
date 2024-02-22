import base64

import requests
from django.conf import settings

from report_a_breach.exceptions import CompaniesHouseException

COMPANIES_HOUSE_BASIC_AUTH = base64.b64encode(
    bytes(f"{settings.COMPANIES_HOUSE_API_KEY}:", "utf-8")
).decode("utf-8")
COMPANIES_HOUSE_BASE_DOMAIN = "https://api.companieshouse.gov.uk"


def get_details_from_companies_house(registration_number):
    """
    Retrieves and returns details of a company from Companies House
    using registration number that is passed in.
    """

    get_company_headers = {"Authorization": f"Basic {COMPANIES_HOUSE_BASIC_AUTH}"}
    response = requests.get(
        f"{COMPANIES_HOUSE_BASE_DOMAIN}/company/{registration_number}",
        headers=get_company_headers,
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise CompaniesHouseException(f"Companies House API request failed: {response.status_code}")


def get_formatted_address(address_dict: dict):
    """Get formatted, human-readable address from Companies House address dict."""
    address_string = ""

    line_1 = address_dict["address_line_1"]
    address_string += line_1

    if line_2 := address_dict.get("address_line_2", ""):
        address_string += f", {line_2}"

    country = address_dict["country"]
    address_string += f", {country}"

    postal_code = address_dict["postal_code"]
    address_string += f", {postal_code}"

    return address_string
