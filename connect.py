from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


def main():
    engine = create_engine('sqlite:///college.db', echo = True)
    meta = MetaData()

    students = Table(
       'students', meta, 
       Column('id', Integer, primary_key = True), 
       Column('name', String), 
       Column('lastname', String),
    )
    meta.create_all(engine)

    conn = engine.connect()
    ins = students.insert()
    ins = students.insert().values(name = 'Matthias', lastname = 'Pupillo')
    result = conn.execute(ins)
    ins = students.insert().values(name = 'Not Matthias', lastname = 'NOT Pupillo')
    result = conn.execute(ins)

    s = students.select()
    result = conn.execute(s)

    for row in result:
        print (row)



main()