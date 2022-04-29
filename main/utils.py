import psycopg2
import psycopg2.extras


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