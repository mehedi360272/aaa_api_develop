# -*- coding: utf-8 -*-
from odoo import http
# from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class AaaApiDevelop(http.Controller):
    @http.route('/aaa/api/develop', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        contact_list = http.request.env['res.partner'].sudo().search([])
        return_contact_list = list()
        for contact in contact_list:
            _logger.info(contact.name)
