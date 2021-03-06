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

#Campo Funcional para contar el numero de operarios que realizan un servicio
def _numOperarios(self,cr,uid,ids,field,arg,context= None): #self, cr es la conexion con la base de datos, el uid usuario conectado, ids lista de los registros implicados
        res = { }   #como clave el id del registro a modificar y como valor el valor del campo al que se le asocia
        for servicio in self.browse(cr, uid, ids): #para cada clase busca
            res[servicio.id]= len(servicio.operarios_ids)  #mete en el array el id de la clase asociandole la cantidad de usuarios
            
        return res

class servicio(osv.Model):
    _name = 'servicio'
    _description = 'servicio que realiza un operario'
 
    _columns = {
            'id':fields.char('ID', size=9, required=False),
            'name': fields.char('Name',size=140, required=True),
            'f_creacion':fields.date('Fecha_creacion', size=20, required=True),
            'descripcion':fields.char('Descripcion', size=140, required=True),
            'operarios_ids': fields.many2many( 'operario','operario_servicio_rel',
                                              'servicio_id', 'operario_id', 'Operarios disponibles', required=True),
            'cita_ids': fields.one2many('cita','servicio_id', 'Citas'),
            'numOperarios' :fields.function(_numOperarios,readonly=True,type='integer',store=True,string="Numero de operarios"),
        }