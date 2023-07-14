{
    "name": "qz-tray-odoo",
    "summary": """
        Modulo de impresiones
        Soporte ZPL e impresion remota
        """,
    "description": """
        Modulo de impresiones
        Soporte ZPL e impresion remota
    """,
    "category": "Stock",
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base","product","stock","web","website"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",        
        "views/views.xml",
        "views/qz_template.xml",
    ],
    'license': 'LGPL-3',
    "assets": {
        "web.assets_frontend": [
            "qz-tray-odoo/static/src/js/qz-tray.js",
            "qz-tray-odoo/static/src/js/script.js"
        ]
    } 
}
