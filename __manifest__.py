{
    'name': 'NCC_Database',
    'version': '1.0',
    'summary': 'Reviews Supplier ',
    'category': 'Supplier',
    'author': 'Hieu',
    'depends': ['base'],
    'data': [

        'security/nhom_quan_ly_ncc_.xml',
        'security/ir.model.access.csv',
        'security/phan_quyen_ncc.xml',

        'views/tieu_chi_dg.xml',
        'views/danh_gia_ncc.xml',
        'views/ct_danh_gia_ncc.xml',
        'views/thong_tin_ncc.xml',


        'views/quan_ly_ncc_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'quan_ly_ncc/static/src/css/styles.css',
        ],
    },
}
