from odoo import models, fields, api

class CtDanhGiaNcc(models.Model):
    _name = 'ct.danh.gia.ncc'
    _description = 'Chi tiết đánh giá nhà cung cấp'

    ct_danh_gia_ncc = fields.Many2one('danh.gia.ncc', string='Đánh giá nhà cung cấp')
    tieu_chi_dg = fields.Many2one('tieu.chi.dg', string='Tiêu chí đánh giá')
    da_duoc_dg = fields.Boolean(string='Đã được đánh giá')
    diem_dg = fields.Selection([
        ('0', '0 sao'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao'),
    ], string='Điểm đánh giá')
    tong_diem_cuoi_cung = fields.Float(string='Tổng điểm cuối cùng', compute='_compute_tong_diem_cuoi_cung')
    kq_danh_gia = fields.Selection([
        ('0', '0 sao'),
        ('1', '1 sao'),
        ('2', '2 sao'),
        ('3', '3 sao'),
        ('4', '4 sao'),
        ('5', '5 sao'),
    ], string='Kết quả đánh giá',compute='_compute_kq_danh_gia')
    thong_tin_phan_hoi = fields.Text(string='Thông tin phản hồi')
    user_id = fields.Many2one('res.users', string='User')

    @api.depends('diem_dg')
    def _compute_tong_diem_cuoi_cung(self):
        for record in self:
            total_score=0
            count=0
            for detail in record.ct_danh_gia_ncc.ct_danh_gia_chi_tiet_ids:
                total_score+=int(detail.diem_dg)
                count+=1
            if count>0:
                record.tong_diem_cuoi_cung=total_score/count
            else :
                record.tong_diem_cuoi_cung=0

    @api.depends('tong_diem_cuoi_cung')
    def _compute_kq_danh_gia(self):
        for record in self:
            if record.tong_diem_cuoi_cung >= 4.5:
                record.kq_danh_gia = '5'
            elif record.tong_diem_cuoi_cung >= 3.5:
                record.kq_danh_gia = '4'
            elif record.tong_diem_cuoi_cung >= 2.5:
                record.kq_danh_gia = '3'
            elif record.tong_diem_cuoi_cung >= 1.5:
                record.kq_danh_gia = '2'
            elif record.tong_diem_cuoi_cung >= 0.5:
                record.kq_danh_gia = '1'
            else:
                record.kq_danh_gia = '0'
