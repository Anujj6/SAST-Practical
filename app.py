import sqlite3

def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    return result

password = "admin123"

print(get_user("admin"))
