from odoo import models, fields, api


class DanhGiaNCC(models.Model):
    _name = 'danh.gia.ncc'
    _description = 'Đánh giá nhà cung cấp'
    _rec_name = 'ma_phieu'

    ma_phieu = fields.Char(string='Mã phiếu', readonly=True)
    ten_ncc = fields.Many2one('thong.tin.ncc', string='Thông tin ncc')
    email = fields.Char(string='Email', required=True)
    dien_thoai = fields.Integer(string='Điện thoại')
    nganh_kd = fields.Char(string='Ngành kinh doanh')
    ky_dg = fields.Date(string='Kỳ đánh giá')
    ngay_dg = fields.Date(string='Ngày đánh giá')
    quan_ly = fields.Many2one('res.users', string='Quản lý')
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('waiting', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('rejected', 'Từ chối'),
        ('cancelled', 'Huỷ')
    ], string='Trạng thái',default='draft')
    user_id = fields.Many2one('res.users', string='User')

    ct_danh_gia_chi_tiet_ids = fields.One2many(
        'ct.danh.gia.ncc', 'ct_danh_gia_ncc',string='')

    tong_diem_cuoi_cung = fields.Float(
        string='Tổng điểm cuối cùng',
        related='ct_danh_gia_chi_tiet_ids.tong_diem_cuoi_cung'
    )
    kq_danh_gia = fields.Selection([
        ('0', '0 sao'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao'),
    ], string='Kết quả đánh giá', related='ct_danh_gia_chi_tiet_ids.kq_danh_gia')


    @api.model
    def create(self, vals):
        if 'ma_phieu' not in vals:
            vals['ma_phieu'] = self.env['ir.sequence'].next_by_code('dg_ncc') or 'DGNCC0001'

        return super(DanhGiaNCC, self).create(vals)

    def action_confirm(self):
        self.trang_thai = 'confirmed'

    def action_validate(self):
        self.trang_thai = 'waiting'

    def action_reject(self):
        self.trang_thai = 'rejected'

    def action_cancel(self):
        self.trang_thai = 'cancelled'

    def action_draft(self):
        self.trang_thai = 'draft'
