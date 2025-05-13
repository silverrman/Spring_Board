import unittest
from unittest.mock import patch
from app import app

class FlaskAppTestCase(unittest.TestCase):
    """Tests for the Flask application routes and functionality."""
    
    def setUp(self):
        """Set up test client and other test variables."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        
    def test_index_get(self):
        """Test that the index page loads correctly with GET."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Currency Converter', response.data)
        self.assertIn(b'Converting from', response.data)
        
    @patch('app.is_valid_currency')
    def test_invalid_from_currency(self, mock_is_valid_currency):
        """Test handling of invalid 'from' currency."""
        mock_is_valid_currency.side_effect = lambda x: x == 'USD'
        
        response = self.client.post('/', data={
            'from_currency': 'XYZ',
            'to_currency': 'USD',
            'amount': '100'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid currency code: XYZ', response.data)
        
    @patch('app.is_valid_currency')
    def test_invalid_to_currency(self, mock_is_valid_currency):
        """Test handling of invalid 'to' currency."""
        mock_is_valid_currency.side_effect = lambda x: x == 'USD'
        
        response = self.client.post('/', data={
            'from_currency': 'USD',
            'to_currency': 'XYZ',
            'amount': '100'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid currency code: XYZ', response.data)
        
    @patch('app.is_valid_amount')
    def test_invalid_amount(self, mock_is_valid_amount):
        """Test handling of invalid amount."""
        mock_is_valid_amount.return_value = False
        
        response = self.client.post('/', data={
            'from_currency': 'USD',
            'to_currency': 'EUR',
            'amount': 'not-a-number'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Not a valid amount', response.data)
        
    @patch('app.is_valid_currency')
    @patch('app.is_valid_amount')
    @patch('app.convert_currency')
    def test_successful_conversion(self, mock_convert, mock_valid_amount, mock_valid_currency):
        """Test successful currency conversion."""
        mock_valid_currency.return_value = True
        mock_valid_amount.return_value = True
        mock_convert.return_value = (85.16, '€')
        
        response = self.client.post('/', data={
            'from_currency': 'USD',
            'to_currency': 'EUR',
            'amount': '100'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        # Check for each component of the response rather than the exact format
        self.assertIn(b'100', response.data)
        self.assertIn(b'USD', response.data)
        self.assertIn(b'equals', response.data)
        self.assertIn(b'\xe2\x82\xac', response.data)  # Euro symbol
        self.assertIn(b'85.16', response.data)

if __name__ == '__main__':
    unittest.main()
