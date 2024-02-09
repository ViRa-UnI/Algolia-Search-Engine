from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
import logging
import time

_logger = logging.getLogger(__name__)

class TestSearchPerformance(TransactionCase):

    def setUp(self):
        super(TestSearchPerformance, self).setUp()
        # Setup test data if necessary
        self.ProductIndex = self.env['product.index']
        self.SearchAnalytics = self.env['search.analytics']
        # Create a large number of test products to simulate a real-world scenario
        self.create_test_products(1000)

    def create_test_products(self, count):
        for i in range(count):
            self.ProductIndex.create({
                'product_name': 'Test Product {}'.format(i),
                'product_description': 'Description for Test Product {}'.format(i),
                'product_category': 'Category {}'.format(i % 10),
                'product_price': i * 10.0
            })

    def test_search_performance(self):
        """Test that search response time is within acceptable limits."""
        # Define acceptable response time in seconds
        acceptable_response_time = 2.0

        # Simulate a search query
        search_query = "Test Product"
        start_time = time.time()
        products = self.ProductIndex.search([('product_name', 'ilike', search_query)])
        end_time = time.time()

        # Calculate the response time
        response_time = end_time - start_time
        _logger.info('Search response time: %s seconds', response_time)

        # Check if the search response time is acceptable
        self.assertTrue(response_time <= acceptable_response_time,
                        "Search response time exceeds acceptable limits.")

    def tearDown(self):
        # Clean up test data if necessary
        self.ProductIndex.search([]).unlink()
        super(TestSearchPerformance, self).tearDown()

if __name__ == '__main__':
    unittest.main()