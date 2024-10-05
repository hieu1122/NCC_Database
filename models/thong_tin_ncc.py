from odoo import models, fields

class SupplierInfo(models.Model):
    _name = 'thong.tin.ncc'
    _description = 'Thông tin nhà cung cấp'
    _rec_name = 'ten_ncc'

    loai_doi_tuong = fields.Selection([
        ('ca_nhan', 'Cá nhân'),
        ('cong_ty', 'Công ty')
    ],string='Loại đối tuợng', required=True)

    ten_ncc = fields.Char(string='Tên nhà cung cấp', required=True)
    dia_chi = fields.Char(string='Địa chỉ', required=True)
    email = fields.Char(string='Email', required=True)
    dien_thoai = fields.Integer(string='Điện thoại')
    website = fields.Char(string='Website')
    tax_id = fields.Char(string='Tax ID')
    tags = fields.Char(string='Tags')
    danh_gia_cuoi_cung = fields.Selection([
        ('0', '0 sao'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao'),
    ], string='Đánh giá cuối cùng', default='1')

    danh_gia_moi = fields.Char(string='Đánh giá mới')
    user_id=fields.Many2one('res.users',string='User')
    danh_gia_ncc_id=fields.One2many('danh.gia.ncc','ten_ncc',string='Tên nhà cung cấp')
