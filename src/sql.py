import mysql.connector


def send_data_to_sql(jackets_dict):

    # Connect to the database
    connection = mysql.connector.connect(user='root', password='root', host='localhost', database='pp1_codeacademy')

    # Create a cursor
    cursor = connection.cursor()

    # Create a table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS striukes (id INT AUTO_INCREMENT PRIMARY KEY, tipas VARCHAR(255), kaina VARCHAR(45))")

    # Insert the data into the tabl
    for tipas_striukes, kaina_striukes in jackets_dict.items():

        sql = "INSERT INTO striukes (tipas, kaina) VALUES (%s, %s)"
        val = (tipas_striukes, kaina_striukes)
        cursor.execute(sql, val)

    # Commit the changes
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()