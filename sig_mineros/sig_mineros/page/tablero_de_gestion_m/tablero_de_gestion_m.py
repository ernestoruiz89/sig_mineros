
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
	context.pbi = frappe.get_value("Cooperativa de Mineria Artesanal", {"name":"Cooperativa de Mineria Artesanal"}, "pbi")