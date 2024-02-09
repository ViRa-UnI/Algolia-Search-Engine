from odoo import http
from odoo.http import request

class AlgoliaSearchController(http.Controller):

    @http.route('/shop/algolia_search', type='json', auth='public', website=True)
    def search_products(self, search_term, **kwargs):
        search_results = request.env['product.index'].sudo().search_products(search_term)
        return search_results

    @http.route('/shop/update_product_index', type='json', auth='user', website=True)
    def update_product_index(self, **kwargs):
        success = request.env['product.index'].sudo().update_product_index()
        return {'success': success}

    @http.route('/shop/search_analytics', type='http', auth='user', website=True)
    def get_search_analytics(self, **kwargs):
        analytics_data = request.env['search.analytics'].sudo().get_search_analytics()
        return request.render('module_name.analytics_dashboard_view_template', {
            'analytics_data': analytics_data
        })