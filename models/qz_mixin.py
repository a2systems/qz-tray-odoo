from odoo import _, api, exceptions, fields, models, tools, registry, SUPERUSER_ID
from odoo.exceptions import MissingError, ValidationError

class QzTray(models.AbstractModel):
    _name = 'qz.tray'
    _description = 'qz.tray'

    def _compute_print_url(self):
        for rec in self:
            web_url_param = self.env['ir.config_parameter'].sudo().get_param('web.base.url','')
            if not web_url_param.endswith('/'):
                rec.print_url = web_url_param + '/web/qz-print'
            else:
                rec.print_url = web_url_param + 'web/qz-print'

    print_url = fields.Char('print_url',compute=_compute_print_url)
    zpl_code = fields.Char('ZPL Code')
