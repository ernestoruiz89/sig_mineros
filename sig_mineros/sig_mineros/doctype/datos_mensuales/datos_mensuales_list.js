frappe.listview_settings['Datos Mensuales'] = {
	
	
	refresh(listview) {
		$("[data-view=Calendar]").addClass("hide");
		console.log("Calendario escondido");
		$("[data-view=Kanban]").addClass("hide");
		console.log("kanban escondido")
	},
	
	hide_name_column: true
	
};