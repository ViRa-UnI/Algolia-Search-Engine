from odoo import models, fields

class ProductIndex(models.Model):
    _name = 'product.index'
    _description = 'Product Index for Algolia Search'

    product_name = fields.Char(string='Product Name', required=True, index=True)
    product_description = fields.Text(string='Product Description')
    product_category = fields.Many2one('product.category', string='Product Category')
    product_price = fields.Float(string='Product Price', digits='Product Price')
    # Additional fields can be added as per Algolia's index requirements
    # For example, image fields, tags, or any other attribute that needs to be indexed

    def create_index(self):
        # Logic to create index on Algolia
        pass

    def update_index(self):
        # Logic to update index on Algolia when product details change
        pass

    def delete_index(self):
        # Logic to delete index on Algolia when product is deleted
        pass

    def synchronize_with_algolia(self):
        # Logic to synchronize product data with Algolia
        pass
