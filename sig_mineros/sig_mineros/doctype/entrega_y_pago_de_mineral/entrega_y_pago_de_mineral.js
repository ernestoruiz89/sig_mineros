// Copyright (c) 2019, Ernesto Ruiz Escorcia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Entrega y Pago de Mineral', {	
			
		onzas_oro: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		tipo_de_cambio: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		precio_internacional_oro: function(frm) {	
			cur_frm.cscript.update_totals(frm);				
		},		
		precio_internacional_plata: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		porcentaje_pago: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		deducir_ir: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		deducir_alcaldia: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		validate:function(frm) {	
			cur_frm.cscript.update_totals(frm);
		}
});

frappe.ui.form.on('SM_Deducciones', {
		valor: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		es_reembolsable: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		deducciones_add: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		deducciones_remove: function(frm) {	
			cur_frm.cscript.update_totals(frm);
		},
		validate:function(frm) {	
			cur_frm.cscript.update_totals(frm);
		}
});


cur_frm.cscript.update_totals = function(frm) {
	var ingreso_oro_val = frm.doc.onzas_oro*frm.doc.precio_internacional_oro*frm.doc.tipo_de_cambio;
	var ingreso_plata_val = frm.doc.onzas_oro*frm.doc.precio_internacional_plata*frm.doc.tipo_de_cambio;
	var ingreso_total_val = ingreso_oro_val + ingreso_plata_val;
	var pago_minero_val =  ingreso_total_val * frm.doc.porcentaje_pago/100;
	
	frm.set_value("ingreso_oro", ingreso_oro_val);
	frm.set_value("ingreso_plata", ingreso_plata_val);
	frm.set_value("ingreso_total", ingreso_total_val);
	frm.set_value("pago_minero", pago_minero_val);


	var td=0.0;
	var deducciones = frm.doc.deducciones || [];
	for(var i in deducciones) {
		td += flt(deducciones[i].valor, precision("valor", deducciones[i]));
	}
	frm.set_value("total_deducciones", td);
	
	
	if(frm.doc.deducir_ir == true){
		var impuesto_ir_val = pago_minero_val*0.02;
		frm.set_value("impuesto_ir", impuesto_ir_val);
	} else{
		var impuesto_ir_val = 0.00;
		frm.set_value("impuesto_ir", impuesto_ir_val);
	}
	
	if(frm.doc.deducir_alcaldia == true){
		var impuesto_alcaldia_val = pago_minero_val*0.01;
		frm.set_value("impuesto_alcaldia",impuesto_alcaldia_val);
	} else{
		impuesto_alcaldia_val = 0.00;
		frm.set_value("impuesto_alcaldia", impuesto_alcaldia_val);
	}
	
	frm.set_value("pago_neto", pago_minero_val-td-impuesto_ir_val-impuesto_alcaldia_val);

	var tr=0.0;
	var deducciones = frm.doc.deducciones || [];
	if(deducciones){
		deducciones.forEach(function(d) {
			if(d.es_reembolsable == true) {
				 tr += d.valor;
			}
		});
	}

	frm.set_value("a_reembolsar", tr);
	
}