from odoo import api, fields, models
from odoo.exceptions import UserError

class AlgoliaConfigWizard(models.TransientModel):
    _name = 'algolia.config.wizard'
    _description = 'Algolia Configuration Wizard'

    algolia_application_id = fields.Char(string='Algolia Application ID', required=True)
    algolia_api_key = fields.Char(string='Algolia API Key', required=True)
    algolia_index_name = fields.Char(string='Algolia Index Name', required=True)

    @api.model
    def default_get(self, fields_list):
        res = super(AlgoliaConfigWizard, self).default_get(fields_list)
        # Retrieve and set default values from system parameters or other sources if necessary
        # Example:
        # res['algolia_application_id'] = self.env['ir.config_parameter'].sudo().get_param('algolia_application_id')
        return res

    def apply_configuration(self):
        self.ensure_one()
        # Validate Algolia credentials and connectivity
        if not self.algolia_application_id or not self.algolia_api_key:
            raise UserError('Algolia Application ID and API Key are required.')

        # Save the configuration to system parameters or a dedicated config model
        # Example:
        # self.env['ir.config_parameter'].sudo().set_param('algolia_application_id', self.algolia_application_id)
        # self.env['ir.config_parameter'].sudo().set_param('algolia_api_key', self.algolia_api_key)
        # self.env['ir.config_parameter'].sudo().set_param('algolia_index_name', self.algolia_index_name)

        # Perform any additional setup required, such as initializing the Algolia index
        # Example:
        # algolia_client = AlgoliaClient(self.algolia_application_id, self.algolia_api_key)
        # algolia_client.init_index(self.algolia_index_name)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }