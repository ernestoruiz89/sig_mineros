# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ernesto Ruiz Escorcia and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import utils
from frappe.utils import getdate
from frappe.model.document import Document
import datetime

class EntregayPagodeMineral(Document):
	
	def validate(self):
		
		es_activo = frappe.db.get_value("Minero Artesanal", {"name": self.minero_artesanal}, "es_activo")
		fecha_salida = frappe.db.get_value("Minero Artesanal", {"name": self.minero_artesanal}, "fecha_salida")
		fecha_ingreso = frappe.db.get_value("Minero Artesanal", {"name": self.minero_artesanal}, "fecha_ingreso")
		fecha_constitucion = frappe.db.get_single_value('Cooperativa de Mineria Artesanal', 'fecha_constitucion')
		
		
		fecha_entrega = getdate(self.fecha_entrega)
		
		today = getdate(utils.today())
		if  fecha_entrega > today:
			frappe.throw("La fecha de entrega ({0}) no puede ser mayor al dia de hoy ({1})".format(fecha_entrega, today),title="Fecha Inválida")
		
		#if fecha_salida:
			#if not es_activo and fecha_salida <= fecha_entrega:
				#frappe.throw("El socio <strong>{0}</strong> no se encuentra activo, verifique su estatus con la Cooperativa.".format(self.nombre_minero_artesanal))
		
		if not es_activo:
			frappe.throw("El socio <strong>{0}</strong> no se encuentra activo, verifique su estatus con la Cooperativa.".format(self.nombre_minero_artesanal))
			
		#if fecha_ingreso:
			#if fecha_entrega < fecha_ingreso:
				#frappe.throw("La fecha de entrega ({0}) es menor a la fecha de ingreso ({1}) del socio <strong>{2}</strong> a la #Cooperativa.".format(fecha_entrega,fecha_ingreso, self.nombre_minero_artesanal),title="Fecha Inválida")		
			
		
		#if fecha_constitucion:
			#fc = getdate(fecha_constitucion)
			#if fecha_entrega < fc:
				#frappe.throw("La fecha de entrega ({0}) es menor a la fecha de constitución ({1}) de la cooperativa.".format(fecha_entrega,fc),title="Fecha #Inválida")
		
		
		if self.tiene_colilla:
			
			if self.toneladas_aceptadas > self.toneladas_entregadas:
				frappe.throw("Las toneladas aceptadas ({0} Ton) no pueden ser mayor a las toneladas entregadas ({1} Ton)".format(self.toneladas_aceptadas,self.toneladas_entregadas),title="Datos Inválidos")
				
			if self.fecha_pago:
				fecha_pago = getdate(self.fecha_pago)
				
				if fecha_pago < fecha_entrega:
					frappe.throw("La fecha de pago ({0}) no puede ser menor a la fecha de entrega ({1})".format(fecha_pago,fecha_entrega),title="Fecha Inválida")		
			
				
				if not self.fecha_pago or not self.toneladas_aceptadas or not self.ley or not self.onzas_oro or not self.tipo_de_cambio or not self.precio_internacional_oro or not self.precio_internacional_plata:
					frappe.throw("Debe llenar todos los campos requeridos del comprobante de pago",title="Completar datos")
