# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ernesto Ruiz Escorcia and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DatosMensuales(Document):
	pass
	
@frappe.whitelist()
def nuevos_socios_anio(anio):

	nuevos_socios = frappe.db.sql("""select sum(nuevos_socios) from `tabDatos Mensuales` where anio=%s""", (anio))
	
	return nuevos_socios

@frappe.whitelist()
def salida_socios_anio(anio):

	nuevos_socios = frappe.db.sql("""select sum(nuevos_socios) from `tabDatos Mensuales` where anio=%s""", (anio))
	
	return salida_socios
