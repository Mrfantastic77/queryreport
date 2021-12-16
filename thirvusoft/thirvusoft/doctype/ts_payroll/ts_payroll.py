# Copyright (c) 2021, thirvusoft and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ts_payroll(Document):
	def validate(self):
		dict1={"hr":50000,"developer":30000,"trainee":8000,"designer":30000}
		self.basic_pay=dict1[self.role]
		self.pf=self.basic_pay*0.08
		self.da=self.basic_pay*0.02