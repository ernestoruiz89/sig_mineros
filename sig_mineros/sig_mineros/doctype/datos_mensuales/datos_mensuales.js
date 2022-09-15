// Copyright (c) 2020, Ernesto Ruiz Escorcia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Datos Mensuales', {
	validate: function(frm) {
		
		
		cur_frm.cscript.update_fields(frm);
		cur_frm.cscript.update_date(frm);

		if(!frm.doc.__islocal) {
			frappe.call({
				method: "sig_mineros.sig_mineros.doctype.datos_mensuales.datos_mensuales.nuevos_socios_anio", //dotted path to server method
				args: { 
					anio: frm.doc.anio 
				},
				callback: function(r) {
					frm.set_value("nuevos_socios_anio", r.message.toString())
				}		
			});
		}

	}
});


cur_frm.cscript.update_fields = function(frm) {
	
	var socios_inicio_anio = frm.doc.socios_activos+frm.doc.saldida_socios-frm.doc.nuevos_socios;
	var tr = (frm.doc.socios_activos-frm.doc.nuevos_socios)/socios_inicio_anio;
	
	frm.set_value("tasa_retencion", tr);	
	
}

cur_frm.cscript.update_date = function(frm) {
	var mes = frm.doc.mes;
	var anio = frm.doc.anio;

	switch (mes) {

		case "Enero":
		var mes = '01';
		break;

		case "Febrero":
		var mes = '02';
		break;

		case "Marzo":
		var mes = '03';
		break;

		case "Abril":
		var mes = '04';
		break;

		case "Mayo":
		var mes = '05';
		break;
		
		case "Junio":
		var mes = '06';
		break;

		case "Julio":
		var mes = '07';
		break;

		case "Agosto":
		var mes = '08';
		break;

		case "Septiembre":
		var mes = '09';
		break;

		case "Octubre":
		var mes = '10';
		break;

		case "Noviembre":
		var mes = '11';
		break;

		case "Diciembre":
		var mes = '12';
		break;	
	}

	function getDaysInMonth(m, y) {
		return m===2 ? y & 3 || !(y%25) && y & 15 ? 28 : 29 : 30 + (m+(m>>3)&1);
	}

	var dia = getDaysInMonth(mes, anio);
	
	frm.set_value("fecha_cierre", anio+"/"+mes+"/"+dia);
}