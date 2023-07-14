from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval
import requests
import base64

class ZplReport(models.Model):
    _name = "zpl.report"
    _description = "Reporte ZPL"

    @api.constrains('copies')
    def check_copies(self):
        if self.copies < 1:
            raise ValidationError('La cantidad de copias debe ser mayor a 0')

    name = fields.Char("Reporte ZPL",required=True)
    code = fields.Char('Codigo')
    zpl = fields.Text('ZPL')
    copies = fields.Integer('Copias',default=1)
    model_id = fields.Many2one('ir.model','Modelo')
    line_ids = fields.One2many(comodel_name='zpl.report.line',inverse_name='zpl_report_id')

    def print_label(self, obj=None):
        # adjust print density (8dpmm), label width (4 inches), label height (6 inches), and label index (0) as necessary
        url = 'http://api.labelary.com/v1/printers/8dpmm/labels/6x6/0/'
        zpl = self.zpl
        if obj:
            object_read = obj.read()[0]
            for line in self.line_ids:
                if line.variable:
                    if line.field_id.ttype == 'many2one':
                        try:
                            value = str(object_read.get(line.field_id.name,['','N/A'])[1])
                        except:
                            value = 'N/A'
                    else:
                        value = str(object_read.get(line.field_id.name))
                    zpl = zpl.replace(line.variable,value)

        files = {'file' : zpl}
        headers = {'Accept' : 'application/pdf'} # omit this line to get PNG images back
        response = requests.post(url, headers = headers, files = files, stream = True)

        if response.status_code == 200:
            response.raw.decode_content = True
            return response,zpl


class ZplReportLine(models.Model):
    _name = 'zpl.report.line'
    _description = 'Reporte Linea ZPL'

    name = fields.Char('Campo')
    zpl_report_id = fields.Many2one('zpl.report','Reporte ZPL')
    field_id = fields.Many2one('ir.model.fields','Campo')
    variable = fields.Char('Variable')
