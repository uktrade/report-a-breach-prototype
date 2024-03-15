# import os
# from typing import List

# import pytest
# from django.conf import settings
# from django.test.testcases import TransactionTestCase
# from playwright.sync_api import sync_playwright

# from . import types


# class PlaywrightTestBase(TransactionTestCase):
#     create_new_test_breach = True
#     base_url = settings.BASE_FRONTEND_TESTING_URL

#     @classmethod
#     def setUpClass(cls):
#         os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#         super().setUpClass()
#         cls.playwright = sync_playwright().start()
#         cls.browser = cls.playwright.chromium.launch(headless=settings.HEADLESS)

#         if cls.create_new_test_breach:
#             cls.create_test_breach()

#     @classmethod
#     def tearDownClass(cls):
#         cls.browser.close()
#         cls.playwright.stop()

#         super().tearDownClass()

#     def setUp(self) -> None:
#         """Create a new page for each test"""
#         self.page = self.browser.new_page()

#     def tearDown(self) -> None:
#         """Close the page after each test"""
#         self.page.close()

#     @classmethod
#     def get_form_step_page(cls, form_step):
#         return f"{cls.base_url}/{form_step}/"

#     # @classmethod
#     # def fill_uk_address(cls, form_step):
#     #     cls.page.get_by_label("Name of business or person").click()
#     #     page.get_by_label("Name of business or person").fill("Business")
#     #     page.get_by_label("Name of business or person").press("Tab")
#     #     page.get_by_label("Website address").fill("business.com")
#     #     page.get_by_label("Website address").press("Tab")
#     #     page.get_by_label("Address line 1").fill("A1")
#     #     page.get_by_label("Address line 1").press("Tab")
#     #     page.get_by_label("Address line 2").fill("A2")
#     #     page.get_by_label("Address line 2").press("Tab")
#     #     page.get_by_label("Town or city").fill("Town")
#     #     page.get_by_label("Town or city").press("Tab")
#     #     page.get_by_label("County").fill("County")
#     #     page.get_by_label("County").press("Tab")
#     #     page.get_by_label("Postal code").fill("AA0 0AA")
#     #     page.get_by_role("button", name="Continue").click()

#     @classmethod
#     def create_test_breach(cls):
#         new_browser = cls.playwright.chromium.launch(headless=True)
#         context = new_browser.new_context()
#         page = context.new_page()
#         page.goto(cls.base_url)

#         #
#         # Start page
#         #
#         page.get_by_label("I'm an owner, officer or").check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Email page
#         #
#         page.get_by_label("What is your email address?").click()
#         page.get_by_label("What is your email address?").fill("test@digital.gov.uk")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Verify Page
#         #
#         page.get_by_label("We've sent you an email").click()
#         page.get_by_label("We've sent you an email").fill("012345")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Name Page
#         #
#         page.get_by_label("What is your full name?").click()
#         page.get_by_label("What is your full name?").fill("John Smith")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Reporting Business on Companies House Page
#         #
#         page.get_by_label("No", exact=True).check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Where is Address of Business Page
#         #
#         page.get_by_label("In the UK").check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Business or Person Details Page
#         #
#         page.get_by_label("Name of business or person").click()
#         page.get_by_label("Name of business or person").fill("Business")
#         page.get_by_label("Name of business or person").press("Tab")
#         page.get_by_label("Website address").fill("business.com")
#         page.get_by_label("Website address").press("Tab")
#         page.get_by_label("Address line 1").fill("A1")
#         page.get_by_label("Address line 1").press("Tab")
#         page.get_by_label("Address line 2").fill("A2")
#         page.get_by_label("Address line 2").press("Tab")
#         page.get_by_label("Town or city").fill("Town")
#         page.get_by_label("Town or city").press("Tab")
#         page.get_by_label("County").fill("County")
#         page.get_by_label("County").press("Tab")
#         page.get_by_label("Postal code").fill("AA0 0AA")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # When Did You First Suspect Page
#         #
#         page.get_by_label("When did you first suspect").click()
#         page.get_by_label("When did you first suspect").fill("July")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Which Sanctions Regime Page
#         #
#         page.get_by_label("The test 3 full name").check()
#         page.get_by_label("The test 2 full name").check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # What Were the Goods Page
#         #
#         page.get_by_label("What were the goods or").click()
#         page.get_by_label("What were the goods or").fill("goods")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Where Were the Goods Supplied From Page
#         #
#         page.get_by_label("A1, A2, AA0 0AA, GB").check()
#         page.get_by_role("button", name="Continue").click()
#         page.get_by_label("The UK", exact=True).check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # About the Supplier Page
#         #
#         page.get_by_label("Name of person").click()
#         page.get_by_label("Name of person").fill("Person 1")
#         page.get_by_label("Name of person").press("Tab")
#         page.get_by_label("Name of business").fill("Business 2")
#         page.get_by_label("Name of business").press("Tab")
#         page.get_by_label("Email").fill("business2@email.com")
#         page.get_by_label("Email").press("Tab")
#         page.get_by_label("Website address").press("Tab")
#         page.get_by_label("Address line 1").fill("AL1")
#         page.get_by_label("Address line 1").press("Tab")
#         page.get_by_label("Address line 2").fill("AL2")
#         page.get_by_label("Address line 2").press("Tab")
#         page.get_by_label("Town or city").fill("Town")
#         page.get_by_label("Town or city").press("Tab")
#         page.get_by_label("Town or city").click()
#         page.get_by_label("Town or city").fill("Town2")
#         page.get_by_label("County").click()
#         page.get_by_label("County").fill("County2")
#         page.get_by_label("County").press("Tab")
#         page.get_by_label("Postal code").fill("AA0 0AA")
#         page.get_by_label("Postal code").press("Tab")
#         page.get_by_label("Additional contact details").fill("contact")
#         page.get_by_label("Additional contact details").press("Tab")
#         page.get_by_role("button", name="Continue").press("Enter")
#         #
#         #
#         #
#         page.get_by_label("No").check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Were There Other Addresses in the Supply Chain Page
#         #
#         page.get_by_label("No", exact=True).check()
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Upload Documents Page
#         #
#         page.get_by_label("Upload documents (optional)").click()
#         # page.get_by_label("Upload documents (optional)").set_input_files("Photos Library.photoslibrary.zip")
#         page.get_by_role("button", name="Continue").click()
#         #
#         # Tell Us About Suspected Breach Page
#         #
#         page.get_by_label("Tell us about the suspected").click()
#         page.get_by_label("Tell us about the suspected").fill("hj")
#         page.get_by_role("button", name="Continue").click()

#         # #
#         # # Summary Page
#         # #
#         # page.get_by_role("button", name="Continue").click()
#         # page.get_by_label("I agree and accept").check()
#         # page.get_by_role("button", name="Continue").click()
#         # #
#         # # Declaration Page
#         # #
#         # page.get_by_role("heading", name="Submission complete").click()
#         # page.get_by_text("Your reference number").click()
#         # page.get_by_role("heading", name="What happens next").click()
#         # page.get_by_text("We’ve sent your report to the").click()

#         context.close()
#         new_browser.close()


# @pytest.fixture()
# def sample_upload_file() -> List[types.FilePayload]:
#     return [{"name": "test.txt", "mimeType": "text/plain", "buffer": b"test"}]
