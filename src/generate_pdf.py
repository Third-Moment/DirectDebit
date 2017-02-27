


from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes  import letter
from reportlab.lib.pagesizes  import landscape
from reportlab.platypus import Image, Table

import time
import csv
import os

# files and images for function
data_file  = 'data.csv'
print(os.path.abspath(os.path.curdir))
print(os.path.isfile("generic-logo-hi.png"))
pdf_file_name = 'test_combined_output.pdf'
home_map = "test_image.png"
office_map = "test_image.png"
home_locations = "home_locations.csv"




# function that takes dataframe and images and produces pdf
def generate_certificate(data_file, pdf_file_name, home_map, home_locations, office_map):
	c = canvas.Canvas(pdf_file_name, pagesize=letter)
	with open(data_file) as csvfile:
		employee_data = csv.reader(csvfile)
		next(employee_data)
		row_count = 0
		for row in employee_data:
			row_count += 1
			last_name = row[2]
			first_name = row[1]
			address = row[6] + " " + row[7] + " " + row[8] + " " + row[9]
			pdf_file_name = last_name + "_" + first_name + ".pdf"

			attendee_name = first_name + " " + last_name
			
			# Add Generic Company logo for the lolz
			company_logo = "generic-logo-hi.png"
			c.drawImage(company_logo, 15, 750, width=100, height=30)
			# header text
			c.setFont("Helvetica-Bold", 20, leading=None)
			c.drawCentredString(380, 755, "Direct Debit Banking Services Locations")

			# add footer with time
			formatted_time = time.ctime()
			c.setFont("Helvetica", 10, leading=None)
			c.drawCentredString(520, 15, formatted_time)

			# add office details and map image
			c.drawImage(office_map, 25, 125, width=200, height=200)

			# add home details and map image
			c.drawImage(home_map, 25, 400, width=200, height=200)
			
			
			print("Generating pdf number...%d" % row_count)
			
			# save pdf
			c.showPage()
	print("PDF completed")
	c.save()

generate_certificate(data_file, pdf_file_name, home_map, home_locations, office_map)






