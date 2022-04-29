from flask import Blueprint, render_template, request
import pandas as pd
import pdfkit
from .utils import execute_query


path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)



main = Blueprint('main', __name__)


data = {
    "name": "faiz",
    "Email": "faiz@gmail.com",
    "Phone": "0315843543",
    "City": "karachi",    
}






@main.route("/", methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        frequency = request.form.get("frequency")
        company = request.form.get("company")
        format = request.form.get("format")
        
        print(name)
        print(email)
        print(frequency)
        print(company)
        print(format)
        
        query = "SELECT * from public.tbl_margincall_data WHERE party = 'Jake Bank' LIMIT 100"        
        
        results = execute_query(query)
        
        return render_template("results.html", results=results)

        # df = pd.read_excel("sample.xlsx")
        # df.to_html("file.html")
        # pdfkit.from_file("file.html", "file.pdf", configuration=config)
        
        
        
    
    return render_template("index.html")