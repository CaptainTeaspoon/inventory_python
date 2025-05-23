from django.test import TestCase, Client
from django.urls import reverse
from mainapp.models import Items, Usergroups, Users, Warehouse
from django.contrib.auth.models import User

# Create your tests here.

class ItemCreateFormTest(TestCase):
    def setUp(self):
        # Create necessary related objects
        self.user_group = Usergroups.objects.create(
            name="Test Group"
        )
        
        self.warehouse = Warehouse.objects.create(
            name="Test Warehouse",
            usergroup = self.user_group
        )
        
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            userprofile__usergroup = self.user_group
        )
        

        
        # Create a client for making requests
        self.client = Client()
        
    def test_item_create_form_valid_data(self):
        """Test that the item create form works with valid data"""
        # Count items before submission
        item_count_before = Items.objects.count()
        
        # Prepare form data
        form_data = {
            'name': 'Test Item',
            'barcode': 12345678,
            'cost': 100,
            'expiration_date': '2023-12-31',
            'warehouse': self.warehouse.id,
        }
        
        # Submit the form
        response = self.client.post(reverse('item_create'), data=form_data)
        
        # Check that we were redirected (successful form submission)
        self.assertEqual(response.status_code, 302)
        
        # Check that an item was created
        self.assertEqual(Items.objects.count(), item_count_before + 1)
        
        # Check that the item has the correct data
        new_item = Items.objects.latest('id')
        self.assertEqual(new_item.name, 'Test Item')
        self.assertEqual(new_item.barcode, 12345678)
        self.assertEqual(new_item.cost, 100)
        self.assertEqual(new_item.warehouse, self.warehouse)
    
    def test_item_create_form_invalid_data(self):
        """Test that the item create form properly handles invalid data"""
        # Count items before submission
        item_count_before = Items.objects.count()
        
        # Prepare invalid form data (missing required fields)
        form_data = {
            'name': '',  # Empty name should fail validation
            'barcode': 'not-a-number',  # Should be an integer
            'cost': -5,  # Negative cost might fail validation
        }
        
        # Submit the form
        response = self.client.post(reverse('item_create'), data=form_data)
        
        # Check that the form was not submitted successfully
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        
        # Check that no item was created
        self.assertEqual(Items.objects.count(), item_count_before)
        
        # Check that the form contains error messages
        self.assertContains(response, "This field is required")  # For missing fields
        self.assertContains(response, "Ensure this value is greater than or equal to 0")  # For negative quantity
    
    def test_item_create_form_display(self):
        """Test that the item create form displays correctly"""
        response = self.client.get(reverse('item_create'))
        
        # Check that the page loaded successfully
        self.assertEqual(response.status_code, 200)
        
        # Check that the form is in the response
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="barcode"')
        self.assertContains(response, 'name="cost"')
        self.assertContains(response, 'name="expiration_date"')
        self.assertContains(response, 'name="warehouse"')