frappe.views.calendar["Entrega y Pago de Mineral"] = {
	
	refresh(listview) {
		$("[data-view=Gantt]").addClass("hide");
		$("[data-view=Kanban]").addClass("hide");
	},
	
	field_map: {
		"start": "fecha_entrega",
		"end": "fecha_pago",
		"id": "name",
		"title": "nombre_minero_artesanal"
	},
	options: {
		header: {
			left: 'prev,today,next',
			center: 'title',
			right: 'month week'
		}
	},
	get_events_method: "frappe.desk.calendar.get_events"
};