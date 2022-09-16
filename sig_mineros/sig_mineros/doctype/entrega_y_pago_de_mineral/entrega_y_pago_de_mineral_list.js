frappe.listview_settings['Entrega y Pago de Mineral'] = {
	
	//hide_name_column: true,
	add_fields: ["estado_del_mineral"],
	get_indicator: function (doc) {
		
		 doc.indicator_title = "Estado Mineral";
		 
		if (doc.estado_del_mineral === "Pendiente de Resultados") {
			return [__("Pendiente de Resultados"), "grey", "estado_del_mineral,=,Pendiente de Resultados"];
		} else if (doc.estado_del_mineral === "Aceptado") {
			return [__("Aceptado"), "green", "estado_del_mineral,=,Aceptado"];
			} else if (doc.estado_del_mineral === "Remuestreo/Aceptado"	) {
			return [__("R/Aceptado"), "green", "estado_del_mineral,=,Remuestreo/Aceptado"];
		} else if (doc.estado_del_mineral === "Remuestreo") {
			return [__("Remuestreo"), "blue", "estado_del_mineral,=,Remuestreo"];
		}  else if (doc.estado_del_mineral === "Remuestreo/Rechazado") {
			return [__("R/Rechazado"), "red", "estado_del_mineral,=,Remuestreo/Rechazado"];
		}  else if (doc.estado_del_mineral === "Rechazado por HEMCO") {
			return [__("Rechazado por HEMCO"), "red", "estado_del_mineral,=,Rechazado por HEMCO"];
		}  else if (doc.estado_del_mineral === "Rechazado por Minero Artesanal") {
			return [__("Rechazado por Minero Artesanal"), "orange", "estado_del_mineral,=,Rechazado por Minero Artesanal"];
		} else if (doc.estado_del_mineral === "Remuestreo/No Retirado") {
			return [__("R/No Retirado"), "orange", "estado_del_mineral,=,Remuestreo/No Retirado"];
		} 
	}, 
};