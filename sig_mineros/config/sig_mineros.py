from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Formularios"),
			"items": [
				{
					"type": "doctype",
					"name": "Entrega y Pago de Mineral",
					"label": _("Entrega y Pago de Mineral"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Minero Artesanal",
					"label": _("Minero Artesanal (Socios)"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Datos Mensuales",
					"label": _("Datos Estadísticos"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Datos Estados Financieros",
					"label": _("Datos Estados Financieros"),
					"onboard": 1,
				},				
				{
					"type": "doctype",
					"name": "Registro de Accidentes",
					"label": _("Registro de Accidentes"),
					"onboard": 1,
				},			
				
			]
		},
		{
			"label": _("Catálogos"),
			"items": [
				{
					"type": "doctype",
					"name": "Plantel de Entrega",
					"label": _("Plantel de Entrega")
				},
				{
					"type": "doctype",
					"name": "Cargo JD",
					"label": _("Cargos Para Junta Directiva")
				},
				{
					"type": "doctype",
					"name": "Tipo Deducciones",
					"label": _("Tipos de Deducciones en Colilla de Pago de Mineral")
				},
				{
					"type": "doctype",
					"name": "Tipo Cuenta por Cobrar",
					"label": _("Tipos de Cuenta por Cobrar")
				},
				{
					"type": "doctype",
					"name": "Tipo Cuenta por Pagar",
					"label": _("Tipo Cuenta por Pagar")
				},
				{
					"type": "doctype",
					"name": "Tipo de Ingresos",
					"label": _("Tipo de Ingresos")
				},
				{
					"type": "doctype",
					"name": "Tipo de Costos",
					"label": _("Tipo de Costos")
				}
			]
		},		
		{
			"label": _("Configuración"),
			"items": [
				{
					"type": "doctype",
					"name": "Cooperativa de Mineria Artesanal",
					"label": _("Configuración de la Cooperativa"),
					"onboard": 1,
				}				
			]
		},
		{
			"label": _("Reportes"),
			"items": [
				{
					"type": "page",
					"name": "tablero_de_gestion_m",
					"label": _("Tablero de Gestión"),
				}			
			]
		}
			
	]