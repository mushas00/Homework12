import sqlite3
import pandas as pd

connection = sqlite3.connect('sql/books (1).db')

pd.options.display.max_columns = 10
result = pd.read_sql('SELECT * from authors', connection, index_col=['id'])
print(result)

result2 = pd.read_sql('SELECT * from titles', connection)
print(result2)

df = pd.read_sql('SELECT * From author_ISBN', connection)
print(df.head())

result3 = pd.read_sql('SELECT first, last FROM authors', connection)
print(result3)

result4 = pd.read_sql("""
                        SELECT title, edition, copyright
                        FROM titles
                        WHERE copyright > '2016'
                        """, connection)
print(result4)

result5 = pd.read_sql("""
                        SELECT id, first, last
                        FROM authors
                        WHERE last LIKE 'D%'
                    """, connection, index_col=['id'])
print(result5)

result6 = pd.read_sql("""
                        SELECT id, first, last
                        FROM authors
                        WHERE first LIKE '_b%'
                        """, connection, index_col=['id'])
print(result6)

result7 = pd.read_sql("""
                        SELECT title
                        FROM titles 
                        ORDER BY title ASC
                    """, connection)
print(result7)

result8 = pd.read_sql("""
                        SELECT id, first, last
                        FROM authors
                        ORDER BY last, first
                    """, connection, index_col=['id'])
print(result8)

result9 = pd.read_sql("""
                        SELECT id, first, last
                        FROM authors
                        ORDER BY last DESC, first ASC
                    """, connection)
print(result9)

result10 = pd.read_sql("""
                        SELECT isbn, title, edition, copyright
                        FROM titles
                        WHERE title LIKE '%How to Program'
                        ORDER BY title
                    """, connection)
print(result10)

result11 = pd.read_sql("""
                        SELECT first, last, isbn
                        FROM authors
                        INNER JOIN author_ISBN
                            ON authors.id = author_ISBN.id
                        ORDER BY last, first
                    """, connection)
print(result11.head())

cursor = connection.cursor()
cursor = cursor.execute("""
                            INSERT INTO authors (first, last)
                            VALUES ('Sue', 'Red')
                            """)
result12 = pd.read_sql('SELECT id, first, last FROM authors', connection)
print(result12)

cursor = cursor.execute("""
                            UPDATE authors SET last='Black'
                            WHERE id = 6
                        """)

result13 = pd.read_sql('SELECT id, first, last FROM authors', connection)
print(result13)

cursor = cursor.execute('DELETE FROM authors WHERE id = 6')
result14 = pd.read_sql('SELECT id, first, last FROM authors', connection)
print(result14)

result_a = pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection)
print(result_a)

result_b = pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection)
print(result_b)

query_c = "SELECT titles.title, titles.copyright, titles.isbn " \
          "FROM titles " \
          "INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn " \
          "INNER JOIN authors ON author_ISBN.id = authors.id " \
          "WHERE authors.first = 'Dan' " \
          "ORDER BY titles.title ASC;"
result_c = pd.read_sql(query_c, connection)
print(result_c)

# d. Insert a new author into the authors table.
cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('John', 'Doe')")
print("New author inserted successfully.")

cursor = cursor.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES ('1234567890', 'New Book', 1, 2023)")
cursor = cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (1, '1234567890')")
print("New title added for the author successfully.")

# Insert contacts into the database
insert_query = """
    INSERT INTO contacts (first_name, last_name, phone_number) VALUES
    ('John', 'Doe', '1234567890'),
    ('Jane', 'Smith', '9876543210'),
    ('Michael', 'Johnson', '4567891230');
"""
cursor.execute(insert_query)
connection.commit()
print("Contacts inserted successfully.")

# Query the database to list all contacts
select_all_query = "SELECT * FROM contacts;"
cursor.execute(select_all_query)
all_contacts = cursor.fetchall()
print("All contacts:")
for contact in all_contacts:
    print(contact)

# Query the database to list contacts with a specific last name
specific_last_name = "Smith"
select_specific_query = f"SELECT * FROM contacts WHERE last_name = '{specific_last_name}';"
cursor.execute(select_specific_query)
specific_contacts = cursor.fetchall()
print(f"Contacts with last name '{specific_last_name}':")
for contact in specific_contacts:
    print(contact)

# Update a contact
contact_id_to_update = 1
new_phone_number = '5555555555'
update_query = f"UPDATE contacts SET phone_number = '{new_phone_number}' WHERE id = {contact_id_to_update};"
cursor.execute(update_query)
connection.commit()
print(f"Contact with ID {contact_id_to_update} updated successfully.")

# Delete a contact
contact_id_to_delete = 2
delete_query = f"DELETE FROM contacts WHERE id = {contact_id_to_delete};"
cursor.execute(delete_query)
connection.commit()
print(f"Contact with ID {contact_id_to_delete} deleted successfully.")

# View the contents of the contacts table
select_all_query = "SELECT * FROM contacts;"
cursor.execute(select_all_query)
table_contents = cursor.fetchall()
print("Contents of the 'contacts' table:")
for row in table_contents:
    print(row)


connection.close()
















