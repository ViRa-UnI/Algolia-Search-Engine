from odoo import models, fields

class SearchAnalytics(models.Model):
    _name = 'search.analytics'
    _description = 'Search Analytics Model'

    search_query = fields.Char(string='Search Query', required=True)
    user_interaction = fields.Char(string='User Interaction')
    engagement_metric = fields.Integer(string='Engagement Metric')
    search_date = fields.Datetime(string='Search Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='User')