// Copyright (c) 2016, thirvusoft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Salary Slip1"] = {
	"filters": [
		{
			fieldname:"from_date",
			label:__("fromdate"),
			fieldtype:"Date",
			
		},
		{
			fieldname:"to_date",
			label:__("todate"),
			fieldtype:"Date",
		
		},
		{
			fieldname:"role",
			label:__("role"),
			fieldtype:"Select",
			options: [
				{"value":"hr","label":__("hr")},
				{"value":"designer","label":__("designer")},
				{"value":"developer","label":__("developer")},
				{"value":"trainee","label":__("trainee")}

			]
		},

	]
};
