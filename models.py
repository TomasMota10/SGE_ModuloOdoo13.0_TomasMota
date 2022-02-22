from odoo import models, fields

class ListaMuebles(models.Model):
    _name="lista.muebles"
    nombre = fields.Char("Nombre del mueble")
    descripcion = fields.Char("Descripción del mueble")
    categoria = fields.Selection(selection=[("sofas","Sofás"),("silla","Sillas"),("mesas","Mesas"),("librerias","Librerías"),("camas","Camas")])
    productstatus = fields.Selection(selection=[("nuevo","Nuevo"),("segundamano","Segunda Mano"),("reacondicionado","Reaconcionado")])
    empresaorigen = fields.Char("Empresa de Origen")
    precioventa = fields.Char("Precio de Venta")
   