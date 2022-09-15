import frappe
from frappe import _
from erpnext.setup.utils import insert_record


data = {
	'on_setup': 'sig_mineros.setup.setup_sig_mineros'
}


def setup_sigmineros():
	if frappe.db.exists('Tipo Cuenta por Cobrar', 'HEMCO') and frappe.db.exists('Tipo de Ingresos', 'Otros Ingresos'):
		# already setup
		return
	create_custom_records()


def create_custom_records():
	create_tipo_cuentas_por_cobrar()
	create_tipo_cuentas_por_pagar()
	create_tipo_ingreso()
	create_tipo_costos()


def create_tipo_cuentas_por_cobrar():
	records = [
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "A Clientes", "descripcion": "<div><strong>Cuenta por cobrar a clientes tales como:</strong></div><ul><li>Venta de productos / sacos al crédito</li><li>Factura pendiente de pago</li><li>Nota de crédito</li><li>Cualquier otra cuenta por cobrar a clientes</li></ul>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "A Empleados", "descripcion": "<div><strong>Cuenta por cobrar a empleados tales como:</strong></div><ul><li>Préstamos</li><li>Anticipos</li><li>Faltantes </li><li>Venta de productos / sacos al crédito</li><li>Cualquier otra cuenta por cobrar al personal</li></ul>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "A Particulares", "descripcion": "<div><strong>Cuenta por cobrar a particulares tales como:</strong></div><ul><li>Préstamos</li><li>Anticipos</li><li>Venta de productos / sacos al crédito</li><li>Cualquier otra cuenta por cobrar a particulares</li></ul>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "A Socios", "descripcion": "<div><strong>Cuenta por cobrar a socios tales como:</strong></div><ul><li>Prestamos</li><li>Anticipos</li><li>Venta de productos / sacos al crédito</li><li>Aporte pendiente</li><li>Cualquier otra cuenta por cobrar a socios</li></ul>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "HEMCO", "descripcion": "<div><strong>Cuenta por cobrar a HEMCO tales como:</strong></div><ul><li>Colilla pendiente de pago (Lo referente al aporte deducido a socio)</li><li>Aporte / viático como apoyo a la cooperativa</li><li>Cualquier otra cuenta por cobrar a HEMCO</li></ul>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "Otra Cooperativa", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo Cuenta por Cobrar", "tipo_cuenta_cobrar": "Otros", "descripcion": "<div><strong>Cuenta por cobrar otros:</strong></div><ul><li>Cualquier otro que no esté descrita en otros tipos de cuenta por cobrar.</li></ul>"},
	]

	insert_record(records)
	
def create_tipo_ingreso():
	records = [
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Aporte de Socios", "descripcion": "<div>Aporte de los socios, pactado en C$1,800 mensual</div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Cosecha", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Mineral (Broza)", "descripcion": "<div>Venta de Mineral (extraídos a título de la cooperativa y no de socios)</div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Otros Ingresos", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Restaurante", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Transporte", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Ingresos", "tipo_ingreso": "Venta de Sacos", "descripcion": "<div>Ingreso por venta de sacos</div>"},
	]

	insert_record(records)
	
#def create_tipo_ingreso():
	#records = [
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
	#	{"doctype": "Tipo de Ingresos", "tipo_ingreso": "", "descripcion": ""},
   # ]

	insert_record(records)

def create_tipo_costos():
	records = [
		{"doctype": "Tipo de Costos", "tipo_costo": "Agricultura", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Carga y Descarga", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Combustibles y Lubricantes", "descripcion": "<div><br></div"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Materiales", "descripcion": "<div>Costo incurrido en compra de materiales para la extracción, ejemplo: sacos, lamparas, palas, picos, baldes, etc.</div>"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Extracción Broza", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Restaurante", "descripcion": "<div><br></div>"},
		{"doctype": "Tipo de Costos", "tipo_costo": "Transporte", "descripcion": "<div>Costo incurrido en trasporte, adicional al cobrado en colilla</div>"},
	]

	insert_record(records)

