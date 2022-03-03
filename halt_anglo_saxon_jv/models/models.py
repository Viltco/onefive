# -*- coding: utf-8 -*-

from odoo import models, fields, api


class halt_anglo_saxon_jv(models.Model):
    _inherit="account.move"
    
#     def action_post(self):
#         res = super(halt_anglo_saxon_jv,self).
    def action_post(self):
        print(self.line_ids)
        res= super(halt_anglo_saxon_jv ,self)._post(soft=False)
        print(self.line_ids)
        
        return res
#         if self.payment_id:
#             self.payment_id.action_post()
#         else:
#             super(halt_anglo_saxon_jv ,self)._post(soft=False)
# #             self._post(soft=False)
#         return False
#     
#     
#     
#     def _post(self, soft=True):
#         # OVERRIDE
#         # Create additional price difference lines for vendor bills.
#         if self._context.get('move_reverse_cancel'):
#             return super()._post(soft)
#         self.env['account.move.line'].create(self._stock_account_prepare_anglo_saxon_in_lines_vals())
#         return super()._post(soft)
#     
#     def _stock_account_prepare_anglo_saxon_in_lines_vals(self):
#         res = super(halt_anglo_saxon_jv,self)._stock_account_prepare_anglo_saxon_in_lines_vals()
#         return res
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
