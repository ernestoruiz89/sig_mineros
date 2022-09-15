frappe.pages['tablero_de_gestion_m'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Tablero de Gestión',
		single_column: true
	});
	
	$(frappe.render_template('tablero_de_gestion_m')).appendTo(page.body);
}