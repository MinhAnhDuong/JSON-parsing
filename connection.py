import psycopg2
import csv

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="12345678", host="127.0.0.1", port="5432")

except Exception:
    print("database connecting ERROR")

cur = conn.cursor()

try:
    cur.execute("CREATE TABLE my_filter(name varchar NOT NULL, cpu varchar, memory_usage varchar, utc_date varchar, status varchar, ip_address varchar);")
except Exception:
    print("creating table ERROR")

with open('filtered_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO my_filter VALUES (%s, %s, %s, %s, %s, %s)", row)


conn.commit()