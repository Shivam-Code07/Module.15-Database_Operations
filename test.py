import psycopg2

conn = psycopg2.connect(dbname="demodb",user="bittu",password="1234",host="localhost",port=5432)


def create():
    cursor = conn.cursor()
    cursor.execute('''create table Student(clg_id int,Name Text,Age int);''')
    print("Table created successfully!")
    conn.commit()
    conn.close()

def data():
    cursor = conn.cursor()
    cursor.execute('''insert into Student(clg_id ,Name ,Age) values (1001,'Shivam',20);''')
    print("Data added successfully!")
    conn.commit()
    conn.close()    

def input_data():
    cursor = conn.cursor()
    clg_id = input(r"Enter the i'd: ") 
    name = input("Enter the Name: ")
    age = input("Entre the age: ")
    query = '''insert into Student(clg_id ,Name ,Age) values (%s,%s,%s);'''
    cursor.execute(query,(clg_id,name,age))
    conn.commit()
    conn.close()    



def extract():
    cursor = conn.cursor()
    cursor.execute('''select * from Student''')
    show = cursor.fetchall()
    print(f'All Table info: {show}')
    conn.commit()
    conn.close()
 


# create()
# data()
# input_data()
extract()


