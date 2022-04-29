from flask import Blueprint, render_template, request
import pandas as pd
import pdfkit
from .utils import execute_query


path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)



main = Blueprint('main', __name__)


columns = [
    'Bussiness State', 'Agreement Amp Id', 'Party', 'Counterparty',
    'Direction', 'Call Currency', 'Disputed Time', 'Agreed Time',
    'Pledge Accepted Time', 'Pledge Time', 'Sent Time', 'Call Total Call Amount',
    'Valuation Date', 'Call Agreed Amount', 'Call Difference Amount', 
    'Agreement Type', 'Entity', 'Agreement Short Name', 'CP Entity', 
    'CP Agreement Short Name', 'Margincallampid', 'Call Type', 'Exposure',
    'Call Mta', 'CD Exposure', 'Collateral', 'CP Collateral', 'Conversion Rate',
    'USD Mta', 'USD Exposure', 'USD Call Amount', 'USD Collateral', 'USD CP Collateral',
    'USD Threshold', 'USD Call Agreed', 'Issue Time', 'Call to pledge', 
    'Pledge To Accept', 'Call To Agree', 'Call Complete', 'Difference Amount',
    'Difference Rate', 'Call Delivery Type', 'Role', 'CP Role', 'Modify Date'
    
    
]





@main.route("/", methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        frequency = request.form.get("frequency")
        company = request.form.get("company")
        format = request.form.get("format")
        
        query = "SELECT * from public.tbl_margincall_data WHERE party = 'Jake Bank' LIMIT 100"        
        
        results = execute_query(query)
        
        df = pd.DataFrame(results, columns=columns)
        df.to_csv("newresults.csv", index=False)
        
        return render_template("results.html", results=results)



        # df = pd.read_excel("sample.xlsx")
        # df.to_html("file.html")
        # pdfkit.from_file("file.html", "file.pdf", configuration=config)
        
        
        
    
    return render_template("index.html")