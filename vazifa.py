import psycopg2 

db = psycopg2.connect(
    database='FN27',
    user='postgres',
    host='localhost', 
    password='1'
)
cursor = db.cursor()

cursor.execute('''
    drop table if exists schools CASCADE;
    drop table if exists teachers CASCADE;
    drop table if exists students CASCADE;
    drop table if exists classes CASCADE;
    drop table if exists enrollments CASCADE;
    drop table if exists grades CASCADE;
    drop table if exists attendance CASCADE;
    drop table if exists subjects CASCADE;
''')

cursor.execute('''
        create table if not exists schools (
        school_id serial primary key,
        name TEXT NOT NULL,
        address TEXT,
        contact_number CHAR(15),
        davlat_maktabi BOOL
    );
    
    
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id serial primary key,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        contact_number CHAR(15),
        school_id INT REFERENCES schools(school_id)
    );
    
    
    CREATE TABLE IF NOT EXISTS students (
        student_id serial primary key,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob DATE,
        school_id INT REFERENCES schools(school_id),
        gender CHAR(1)
    );
    
    
    CREATE TABLE IF NOT EXISTS classes (
        class_id serial primary key,
        name TEXT NOT NULL,
        teacher_id INT REFERENCES teachers(teacher_id),
        school_id INT REFERENCES schools(school_id)
    );
    
    
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id serial primary key
        name TEXT NOT NULL,
        class_id INT REFERENCES classes(class_id),
        teacher_id INT REFERENCES teachers(teacher_id)
    );

    
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id serial primary key,
        student_id INT REFERENCES students(student_id),
        class_id INT REFERENCES classes(class_id),
        enrollment_date DATE DEFAULT CURRENT_DATE
    );

    CREATE TABLE IF NOT EXISTS grades (
        grade_id serial primary key,
        student_id INT references students(student_id),
        subject_id INT references subjects(subject_id),
        grade_value INT,
        date_given TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id serial primary key,
        student_id INT references students(student_id),
        class_id INT references classes(class_id),
        date DATE DEFAULT CURRENT_DATE
    );
''')

cursor.execute('''
    INSERT INTO schools (name, address, contact_number, davlat_maktabi)
    VALUES 
        ('3 - MAKTAB', 'uchkoprik', '+998770078771', true),
        ('5 - MAKTAB', 'Buvayda', '+998917654321', false);

    INSERT INTO teachers (first_name, last_name, email, contact_number, school_id)
    VALUES 
        ('sobir', 'jalilov', 'sobir@example.com', '+998975647237', 1),
        ('bakir, 'bkirov', 'bakir@example.com', '+998908725491', 2);

    INSERT INTO students (first_name, last_name, dob, gender, school_id)
    VALUES 
        ('Adfghj', 'shodmonov', '2024-08-10', 'M', 1),
        ('Mjhgf', 'jhgfd', '2024-09-12', 'F', 2);

    INSERT INTO classes (name, teacher_id, school_id)
    VALUES 
        ('11-A', 1, 1),
        ('12-B', 2, 2);

    INSERT INTO subjects (name, class_id, teacher_id)
    VALUES 
        ('fizika', 1, 1),
        ('ona tili', 2, 2);

    INSERT INTO enrollments (student_id, class_id)
    VALUES 
        (1, 1),
        (2, 2);

    INSERT INTO grades (student_id, subject_id, grade_value)
    VALUES 
        (1, 1, 90),
        (2, 2, 85);

    INSERT INTO attendance (student_id, class_id)
    VALUES 
        (1, 1),
        (2, 2);
''')

cursor.execute('''
    SELECT enrollment_id, student_id, TO_CHAR(enrollment_date, 'YYYY-MM-DD') AS enrollment_date FROM enrollments;
    SELECT grade_id, student_id, TO_CHAR(date_given, 'YYYY-MM-DD HH24:MI') AS date_given FROM grades;
    SELECT attendance_id, student_id, TO_CHAR(date, 'YYYY-MM-DD') AS date FROM attendance;
''')
products = cursor.fetchall()
for product in products:
    print(product)

cursor.execute('''
    UPDATE schools SET name = '3 - MAKTAB' WHERE school_id = 1;
    UPDATE teachers SET email = first_name || teacher_id || '@gmail.com';  
    UPDATE teachers SET email = 'bakir@example.com' WHERE teacher_id = 1;
    UPDATE classes SET name = '12-B' WHERE class_id = 1;
''')

cursor.execute('''
    DELETE FROM enrollments WHERE enrollment_id = 1;
    DELETE FROM grades WHERE grade_id = 1;
    DELETE FROM attendance WHERE attendance_id = 1;
    DELETE FROM subjects WHERE subject_id = 1;
''')

cursor.execute('''
    ALTER TABLE schools RENAME TO maktab;
    ALTER TABLE teachers RENAME TO oqituvchi;
    ALTER TABLE students RENAME TO oquvchi;
    ALTER TABLE classes RENAME TO classar;
    ALTER TABLE subjects RENAME TO fanlar;
    ALTER TABLE enrollments RENAME TO enrolmantlar;
    ALTER TABLE grades RENAME TO gradeslar;
    ALTER TABLE attendance RENAME TO attendancelar;
''')

cursor.execute('''
    SELECT * FROM maktab;
    SELECT * FROM oqituvchi;
    SELECT * FROM oquvchi;
    SELECT * FROM classar;
    SELECT * FROM fanlar;
    SELECT * FROM enrolmantlar;
    SELECT * FROM gradeslar;
    SELECT * FROM attendancelar;
''')
products = cursor.fetchall()
for i in products:
    print(i)

cursor.execute('''
    drop table if exists maktab CASCADE;
    drop table if exists oqituvchi CASCADE;
    drop table if exists oquvchi CASCADE;
    drop table if exists classar CASCADE;
    drop table if exists fanlar CASCADE;
    drop table if exists enrolmantlar CASCADE;
    drop table if exists gradeslar CASCADE;
    drop table if exists attendancelar CASCADE;
''')

db.commit()
db.close()
