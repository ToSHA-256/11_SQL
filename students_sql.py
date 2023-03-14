import psycopg2

try:
    # Создание соединения с БД
    conn = psycopg2.connect(
        dbname="dbstudents",
        user="sql_user",
        password="sql_password",
        host="localhost",
        port="5432"
    )

    # Открыть курсор для выполнения операций с базой данных
    cur = conn.cursor()

    # SQL-запрос для создания таблицы "student"
    create_table_students = '''
    CREATE TABLE IF not EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        gender VARCHAR(50)
    );
    '''
    create_table_audience = '''
    CREATE TABLE IF not EXISTS audience (
        id SERIAL PRIMARY KEY,
        number INT,
        name VARCHAR(50)
    );
    '''
    # many-to-many relationship
    create_table_audi_stud = '''
    CREATE TABLE IF not EXISTS student_audience (
        audience_id INTEGER REFERENCES audience(id),
        student_id INTEGER REFERENCES students(id),
        PRIMARY KEY(student_id, audience_id)
    );
    '''

    # Выполнить SQL-запрос для создания таблицы
    cur.execute(create_table_students)
    cur.execute(create_table_audience)
    cur.execute(create_table_audi_stud)

    # Зафиксировать изменения в базе данных
    conn.commit()

    cur.execute("INSERT INTO students (name,age,gender) VALUES (%s,%s,%s)", ("Anton", 25, "Male"))
    cur.execute("INSERT INTO students (name,age,gender) VALUES (%s,%s,%s)", ("Mari", 22, "Female"))
    cur.execute("INSERT INTO audience (number,name) VALUES (%s,%s)", (202, "Python"))

    cur.execute("INSERT INTO student_audience (audience_id,student_id) VALUES (%s,%s)", (1, 1))
    cur.execute("INSERT INTO student_audience (audience_id,student_id) VALUES (%s,%s)", (1, 2))

    conn.commit()

    cur.close()
    conn.close()
except BaseException as xcp:
    print("ERROR: " + str(xcp))
else:
    cur.close()
    conn.close()
