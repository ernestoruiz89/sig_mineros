// Copyright (c) 2019, Ernesto Ruiz Escorcia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Minero Artesanal', {
	// refresh: function(frm) {

	// }
	desde_constitucion: function(frm){
		//cur_frm.cscript.desde_constitucion();
	}
	
		
});

 cur_frm.cscript.desde_constitucion = function(frm) {
		 
		var fecha_constitucion = frappe.db.get_single_value('Cooperativa de Mineria Artesanal', 'fecha_constitucion');
		
		alert(fecha_constitucion);
		cur_frm.set_value("fecha_ingreso", fecha_constitucion);
		
	}