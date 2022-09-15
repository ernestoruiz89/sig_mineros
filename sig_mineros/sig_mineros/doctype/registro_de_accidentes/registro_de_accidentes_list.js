frappe.listview_settings['Registro de Accidentes'] = {
	
	
	onload(listview) {
		$("[data-view=Calendar]").addClass("hide");
		$("[data-view=Kanban]").addClass("hide");
	},
	
	hide_name_column: true,
	add_fields: ["tipo_accidente"],
	get_indicator: function (doc) {
		if (doc.tipo_accidente === "Leve") {
			return [__("Leve"), "yellow", "tipo_accidente,=,Leve"];
		} else if (doc.tipo_accidente === "Grave") {
			return [__("Grave"), "orange", "tipo_accidente,=,Grave"];
		} else if (doc.tipo_accidente === "Muy Grave") {
			return [__("Muy Grave"), "red", "tipo_accidente,=,Muy Grave"];
		}  else if (doc.tipo_accidente === "Mortal") {
			return [__("Mortal"), "black", "tipo_accidente,=,Mortal"];
		} 
	}, 
};