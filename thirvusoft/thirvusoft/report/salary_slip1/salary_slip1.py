# Copyright (c) 2013, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _
def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label":_("fromdate"),
			"fieldtype":"Date",
			"fieldname":"from_date",
			"width":100
		},
		{
			"label":_("empname"),
			"fieldtype":"Data",
			"fieldname":"emp_name",
			"width":200
		},
		
		{
			"label":_("todate"),
			"fieldtype":"Date",
			"fieldname":"to_date",
			"width":100
		},
		{
			"label":_("salary"),
			
		},
		{
			"label":_("role"),
			"fieldtype":"Select",
			"options":[
				{"value":"hr","label":("hr")},
				{"value":"designer","label":("designer")},
				{"value":"developer","label":("developer")},
				{"value":"trainee","label":("trainee")}
			]
		},
	]
	return columns
def get_conditions(filters):
	conditions = {}
	if filters.to_date:
		conditions["to_date"] = filters.to_date
	if filters.from_date:
		conditions["from_date"] = filters.from_date
		return conditions

	if filters.role:
		conditions["role"] = filters.role

	return conditions

def get_data(filters):
	data=[]
	conditions=get_conditions(filters)
	accounts=frappe.db.get_all("ts_payroll",fields=["absent_days","from_date","to_date","role","emp_name","basic_pay","pf","da"],filters=conditions)
	salary=0
	for d in accounts:
		salary=(d.basic_pay+d.da-d.pf)-round((d.absent_days*(d.basic_pay/30)),2)
		row={"to_date":d.to_date,"from_date":d.from_date,"role":d.role,"emp_name":d.emp_name,"salary":salary}
		data.append(row)
		salary=0
	return data