import psycopg2
import psycopg2.extras
import pandas as pd
import pdfkit

path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

DB_HOST = "localhost"
DB_NAME = "newdata"
DB_USER = "postgres"
DB_PASS = "faiz"

def execute_query(query):
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute(query)
    
    results = cur.fetchall()
    
    conn.close()
    cur.close()
    return results

def convert_to_pdf(name, df):
    df.to_html(f"{name}.html")
    pdfkit.from_file(f"{name}.html", f"{name}.pdf", configuration=config)

def remove_timezones(df):
    df['Modify Date'] = df['Modify Date'].apply(lambda a: pd.to_datetime(a).date())
    df['Disputed Time'] = df['Disputed Time'].apply(lambda a: pd.to_datetime(a).date())
    df['Agreed Time'] = df['Agreed Time'].apply(lambda a: pd.to_datetime(a).date())
    df['Pledge Accepted Time'] = df['Pledge Accepted Time'].apply(lambda a: pd.to_datetime(a).date())
    df['Pledge Time'] = df['Pledge Time'].apply(lambda a: pd.to_datetime(a).date())
    df['Sent Time'] = df['Sent Time'].apply(lambda a: pd.to_datetime(a).date())
    
    return df


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