import mysql.connector


def send_data_to_sql(jackets_dict):

    # Connect to the database
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='pp1_codeacademy')

    # Create a cursor
    cursor = connection.cursor()

    # Create a table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS jackets (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(255), price VARCHAR(45))")

    # Insert the data into the tabl
    for jacket_type, jacket_price in jackets_dict.items():

        sql = "INSERT INTO jackets (type, price) VALUES (%s, %s)"
        val = (jacket_type, jacket_price)
        cursor.execute(sql, val)

    # Commit the changes
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()