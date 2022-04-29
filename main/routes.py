from flask import Blueprint, render_template, request
import pandas as pd
from .utils import execute_query, convert_to_pdf, columns, remove_timezones



main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        frequency = request.form.get("frequency")
        company = request.form.get("company")
        format = request.form.get("format")
        
        query = f"SELECT * from public.tbl_margincall_data WHERE party = '{company}' LIMIT 100"        
        
        results = execute_query(query)
        
        df = pd.DataFrame(results, columns=columns)
        df = remove_timezones(df)
        if format=='xlsx':
            df.to_excel(f"{name}.xlsx", index=False)
        if format=='csv':
            df.to_csv(f"{name}.csv", index=False)
        if format=='pdf':
            convert_to_pdf(name, df)
        
        return render_template("index.html")



        # df = pd.read_excel("sample.xlsx")
        # df.to_html("file.html")
        # pdfkit.from_file("file.html", "file.pdf", configuration=config)
        
        
        
    
    return render_template("index.html")