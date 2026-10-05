from decimal import Decimal

from django.test import TestCase


class SumaViewTests(TestCase):
    def test_suma_dos_numeros(self):
        response = self.client.post(
            "/suma/",
            {"numero1": "2", "numero2": "3"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["resultado"], Decimal("5"))