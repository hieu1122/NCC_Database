from odoo import api, models,fields

class EvaluationCriteria(models.Model):
    _name = 'tieu.chi.dg'
    _description = 'Tieu Chi Dg'
    _rec_name = 'ten_tc'

    ma_tc=fields.Char(string='Mã Tiêu Chí',required=True)
    ten_tc=fields.Char(string='Tên Tiêu Chí',required=True)
    user_id=fields.Many2one('res.users',string='User')