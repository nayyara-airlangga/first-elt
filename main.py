import csv

from first_elt import db, s3

if __name__ == "__main__":
    db.config_db()
    s3.config_s3()

    conn = db.get_db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()

    with open("data/raw/orders.csv", "w") as f:
        csv_w = csv.writer(f, delimiter='|')
        csv_w.writerows(rows)

    f.close()
    cursor.close()
    conn.close()
