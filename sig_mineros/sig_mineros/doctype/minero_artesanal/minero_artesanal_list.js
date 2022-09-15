frappe.listview_settings['Minero Artesanal'] = {
	
	
	refresh(listview) {
		$("[data-view=Calendar]").addClass("hide");
		console.log("Calendario escondido");
		$("[data-view=Kanban]").addClass("hide");
		console.log("kanban escondido")
	},
	
	hide_name_column: true,
	filters: [["es_activo","=", "1"]],
	
	get_indicator: function (doc) {
		if (doc.es_activo == true) {
			return [__("Activo"), "green", "es_activo,=,true"];
		} else if (doc.es_activo == false) {
			return [__("Inactivo"), "red", "es_activo,=,false"];
		} 
	}
	
};