import unittest
from unittest.mock import patch, MagicMock
from currency_utils import (
    is_valid_currency,
    is_valid_amount,
    get_currency_symbol,
    convert_currency
)

class CurrencyUtilsTestCase(unittest.TestCase):
    """Tests for the currency utility functions."""
    
    def test_is_valid_amount(self):
        """Test validation of amount strings."""
        # Valid amounts
        self.assertTrue(is_valid_amount("100"))
        self.assertTrue(is_valid_amount("0.5"))
        self.assertTrue(is_valid_amount("1000.25"))
        
        # Invalid amounts
        self.assertFalse(is_valid_amount(""))
        self.assertFalse(is_valid_amount("abc"))
        self.assertFalse(is_valid_amount("-100"))  # Negative amount
        self.assertFalse(is_valid_amount("0"))     # Zero amount
        self.assertFalse(is_valid_amount(None))
    
    def test_get_currency_symbol(self):
        """Test retrieval of currency symbols."""
        self.assertEqual(get_currency_symbol("USD"), "$")
        self.assertEqual(get_currency_symbol("EUR"), "€")
        self.assertEqual(get_currency_symbol("GBP"), "£")
        self.assertEqual(get_currency_symbol("JPY"), "¥")
        
        # Unknown currency code should return the code itself
        self.assertEqual(get_currency_symbol("XYZ"), "XYZ")
    
    @patch('requests.get')
    def test_is_valid_currency(self, mock_get):
        """Test validation of currency codes using mocked API responses."""
        # Mock successful API response with valid symbols
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'success': True,
            'symbols': {
                'USD': 'United States Dollar',
                'EUR': 'Euro',
                'GBP': 'British Pound',
            }
        }
        mock_get.return_value = mock_response
        
        # Valid currency codes
        self.assertTrue(is_valid_currency("USD"))
        self.assertTrue(is_valid_currency("EUR"))
        self.assertTrue(is_valid_currency("GBP"))
        
        # Invalid currency code
        self.assertFalse(is_valid_currency("XYZ"))
        
        # Invalid inputs
        self.assertFalse(is_valid_currency(""))
        self.assertFalse(is_valid_currency("US"))  # Too short
        self.assertFalse(is_valid_currency("USDT"))  # Too long
        self.assertFalse(is_valid_currency(None))
        
        # Test API failure
        mock_response.json.return_value = {'success': False}
        self.assertFalse(is_valid_currency("USD"))
        
        # Test exception handling
        mock_get.side_effect = Exception("API error")
        self.assertFalse(is_valid_currency("USD"))
    
    @patch('requests.get')
    def test_convert_currency(self, mock_get):
        """Test currency conversion with mocked API responses."""
        # Mock successful conversion
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'success': True,
            'result': 85.16
        }
        mock_get.return_value = mock_response
        
        # Test successful conversion
        result, symbol = convert_currency("USD", "EUR", 100)
        self.assertEqual(result, 85.16)
        self.assertEqual(symbol, "€")
        
        # Test rounding
        mock_response.json.return_value = {
            'success': True,
            'result': 85.16789
        }
        result, symbol = convert_currency("USD", "EUR", 100)
        self.assertEqual(result, 85.17)  # Check rounding to 2 decimal places
        
        # Test API failure
        mock_response.json.return_value = {'success': False}
        with self.assertRaises(ValueError):
            convert_currency("USD", "EUR", 100)
        
        # Test exception handling
        mock_get.side_effect = Exception("API error")
        with self.assertRaises(ValueError):
            convert_currency("USD", "EUR", 100)

if __name__ == '__main__':
    unittest.main()
