import csv

from first_elt import aws, db

if __name__ == "__main__":
    db.config_db()
    aws.config_aws()

    conn = db.get_db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()

    with open("data/raw/orders.csv", "w") as f:
        csv_w = csv.writer(f)
        csv_w.writerows(rows)

    f.close()
    cursor.close()
    conn.close()

    s3 = aws.new_s3_client()
    s3.upload_file(
        Filename="data/raw/orders.csv",
        Bucket=aws.s3_bucket_name,
        Key="orders.csv",
    )
