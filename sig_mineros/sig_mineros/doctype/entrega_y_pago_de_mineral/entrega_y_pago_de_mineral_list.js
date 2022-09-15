frappe.listview_settings['Entrega y Pago de Mineral'] = {
	
	
	onload(listview) {
		$("[data-view=Kanban]").addClass("hide");
		$("[data-view=Gantt]").addClass("hide");
	},
	
	//hide_name_column: true,
	add_fields: ["estado_del_mineral"],
	get_indicator: function (doc) {
		
		 doc.indicator_title = "Estado Mineral";
		 
		if (doc.estado_del_mineral === "Pendiente de Resultados") {
			return [__("Pendiente de Resultados"), "grey", "estado_del_mineral,=,Pendiente de Resultados"];
		} else if (doc.estado_del_mineral === "Aceptado") {
			return [__("Aceptado"), "green", "estado_del_mineral,=,Aceptado"];
		} else if (doc.estado_del_mineral === "Remuestreo") {
			return [__("Remuestreo"), "blue", "estado_del_mineral,=,Remuestreo"];
		}  else if (doc.estado_del_mineral === "Rechazado por Baja Ley") {
			return [__("Rechazado por Baja Ley"), "red", "estado_del_mineral,=,Rechazado por Baja Ley"];
		}  else if (doc.estado_del_mineral === "Rechazado por Valores Dispersos") {
			return [__("Rechazado por Valores Dispersos"), "red", "estado_del_mineral,=,Rechazado por Valores Dispersos"];
		}  else if (doc.estado_del_mineral === "Rechazado por Minero Artesanal") {
			return [__("Rechazado por Minero Artesanal"), "orange", "estado_del_mineral,=,Rechazado por Minero Artesanal"];
		} 
	}, 
};