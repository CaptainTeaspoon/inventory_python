from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from mainapp.forms import ItemForm
from mainapp.models import Items, Warehouse

# Create your tests here.

class TestItemForm(TestCase):
    def setUp(self):
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.valid_data = {
            'name': 'Test Item',
            'barcode': '1234567890123',
            'cost': 10.99,
            'expiration_date': datetime.now().date() + timedelta(days=30),
            'warehouse': self.warehouse.id
        }

    def test_valid_form(self):
        form = ItemForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = ItemForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_invalid_barcode(self):
        invalid_data = self.valid_data.copy()
        invalid_data['barcode'] = '123'  # Too short
        form = ItemForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('barcode', form.errors)

    def test_negative_cost(self):
        invalid_data = self.valid_data.copy()
        invalid_data['cost'] = -10.99
        form = ItemForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('cost', form.errors)

    def test_past_expiration_date(self):
        invalid_data = self.valid_data.copy()
        invalid_data['expiration_date'] = datetime.now().date() - timedelta(days=1)
        form = ItemForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('expiration_date', form.errors)

    def test_non_existent_warehouse(self):
        invalid_data = self.valid_data.copy()
        invalid_data['warehouse'] = 999  # Non-existent warehouse ID
        form = ItemForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('warehouse', form.errors)
