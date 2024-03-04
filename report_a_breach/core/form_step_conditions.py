def show_check_company_details_page_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("do_you_know_the_registered_company_number") or {}
    return cleaned_data.get("do_you_know_the_registered_company_number", False) and cleaned_data.get(
        "registered_company_number", False
    )


def show_where_is_the_address_of_the_business_or_person_page_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("are_you_reporting_a_business_on_companies_house") or {}
    return cleaned_data.get("business_registered_on_companies_house", False) == "no"


def show_do_you_know_the_registered_company_number_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("are_you_reporting_a_business_on_companies_house") or {}
    return cleaned_data.get("business_registered_on_companies_house", False) in [
        "yes",
        "do_not_know",
    ]


def show_about_the_supplier_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("where_were_the_goods_supplied_from") or {}
    return cleaned_data.get("where_were_the_goods_supplied_from", False) in (
        "different_uk_address",
        "outside_the_uk",
    )


def show_where_were_the_goods_made_available_from_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("where_were_the_goods_supplied_from") or {}
    return cleaned_data.get("where_were_the_goods_supplied_from", False) == "they_have_not_been_supplied"


def show_business_or_personal_details_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("where_is_the_address_of_the_business_or_person") or {}

    # we just want to check that the user has filled out this form as a way of checking if they have filled out the
    # previous form in the chain of conditionals. A -> B -> C. If B is filled out, then A must-have been filled out.
    return cleaned_data.get("where_is_the_address")


def show_name_and_business_you_work_for_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("start") or {}
    return cleaned_data.get("reporter_professional_relationship") in ("third_party", "no_professional_relationship")


def show_name_page(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step("start") or {}
    return cleaned_data.get("reporter_professional_relationship") in ("owner", "acting")