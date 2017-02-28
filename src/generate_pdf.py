


from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes  import letter
from reportlab.lib.pagesizes  import landscape
from reportlab.platypus import Image, Table

import pandas as pd
import time
import os

# files and images for function
data_file  = 'data.csv'
# print(os.path.abspath(os.path.curdir))
# print(os.path.isfile("generic-logo-hi.png"))
pdf_file_name = 'test_combined_output.pdf'
home_map = "test_image.png"
office_map = "test_image.png"

# function that takes dataframe and images and produces pdf
def generate_employee_handout(name, home_address, office_address, home_map, office_map, canvas):
			# Add Generic Company logo for the lolz
			company_logo = "generic-logo-hi.png"
			canvas.drawImage(company_logo, 15, 750, width=100, height=30)
			# header text
			canvas.setFont("Helvetica-Bold", 20, leading=None)
			canvas.drawCentredString(380, 755, "Direct Debit Banking Services Locations")

			# Add name
			canvas.setFont("Helvetica-Bold", 20, leading=None)
			canvas.drawString(25, 700, "Name: " + name)

			# add office details and map image
			canvas.setFont("Helvetica-Bold", 16, leading=None)
			canvas.drawString(25, 630, "Office: " + office_address)
			canvas.drawImage(office_map, 25, 425, width=200, height=200)

			# add home details and map image
			canvas.setFont("Helvetica-Bold", 16, leading=None)
			canvas.drawString(25, 365, "Home: " + home_address)
			canvas.drawImage(home_map, 25, 160, width=200, height=200)
			
			# add footer with time
			formatted_time = time.ctime()
			canvas.setFont("Helvetica", 10, leading=None)
			canvas.drawCentredString(520, 15, formatted_time)

			# save pdf
			canvas.showPage()
			print("PDF completed")


def generate_pdf(data_file, home_map, office_map, pdf_file_name):
	c = canvas.Canvas(pdf_file_name, pagesize=letter)
	data_file = pd.read_csv(data_file)

	for index, row in data_file.iterrows():
		name = row['First_name'] + " " + row['Last_name']
		#print(name)
		home_address = str(row['NUMBER']) + " " + row['STREET'] + " " + row['CITY'] + " " + row['REGION']
		office_address = str(row['OFFICE_NUMBER']) + " " + row['OFFICE_STREET'] + " " + row['OFFICE_CITY'] + " " + row['OFFICE_REGION']
		
		#print(home_address)
		#print(office_address)

		generate_employee_handout(name=name, home_address=home_address, office_address=office_address, home_map=home_map, office_map=office_map, canvas=c)
		#print("Generating pdf number...%d" % data_file.count())
	c.save()




generate_pdf(data_file, home_map, office_map, pdf_file_name)






