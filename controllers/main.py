from odoo import http
from odoo import api, models, _
from odoo.http import request, Response

import logging

_logger = logging.getLogger(__name__)

class Main(http.Controller):

    @http.route('/web/qz-print', type='http',auth='user',website=True,csrf=False)
    def qz_print(self, **kwargs):
        res_id = kwargs.get('res_id','')
        res_model = kwargs.get('res_model','')
        obj = request.env[res_model].browse(int(res_id))
        return request.render('qz-tray-odoo.qz_print_template',{'zpl_code': obj.zpl_code or ''})
