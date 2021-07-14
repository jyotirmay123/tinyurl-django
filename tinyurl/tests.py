from django.test import TestCase


class PaymentTest(TestCase):

    def setUp(self):
        self.payload = {
            "full_url": "https://tier.app/any_long_string"
        }

    def test_index(self):
        response = self.client.post(
            "/tinyurl", data=self.payload, content_type="application/json")
        # After successful execution, there is a redirection to the same page. Thus expecting 301.
        self.assertEqual(response.status_code, 301)

    def test_hits(self):
        response = self.client.get("/tinyurl/tierapp%20abc")
        # In either case there is a redirection. So expecting 302.
        self.assertEqual(response.status_code, 302)
