# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class empresa(osv.Model):

    
    _name = 'empresa'
    _description = 'Empresas que pueden estar relacionadas con el operario'
 
    _columns = {
            'name': fields.char('Company name', size=64, required=True),
            'nif': fields.char('Nif', size=9, required=True),
            'operario_ids': fields.one2many('operario','company_id', 'Operarios')
        }
    
_sql_constraints=[('empresa_nif_uniq','unique (nif)','El nif de la empresa ya existe')]