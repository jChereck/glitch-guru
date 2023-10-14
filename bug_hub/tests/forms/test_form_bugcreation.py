from django.test import TestCase
from django.urls import reverse
from bug_hub.forms import BugCreationForm


class BugCreationFormTestCase(TestCase):
    def setUp(self):
        """
        Create the details of a sample bug instance
        """
        self.data = {
            "title": "Test Bug Title",
            "description": "This is a test bug description.",
            "bug_type": "feature",
            "status": "under_review",
        }

    def test_valid_form_data(self):
        form = BugCreationForm(data=self.data)
        self.assertTrue(form.is_valid(), f"Form is invalid. Errors: {form.errors}")

    def test_valid_form_redirection(self):
        response = self.client.post(
            reverse("bug_hub:bug_create"), data=self.data, follow=True
        )
        self.assertRedirects(response, reverse("bug_hub:bug_list"))

    def test_blank_data(self):
        form = BugCreationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])