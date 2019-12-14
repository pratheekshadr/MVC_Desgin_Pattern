from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, REAL, String, MetaData, ForeignKey
# Global Variables
SQLITE = 'sqlite'

# Table Names
STUDENTDETAILS = 'StudentDetails'
STUDENTGRADES = 'StudentGrades'


class MyDatabase:
    DB_ENGINE = 'sqlite:///{DB}'
    
    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbname):
        engine_url = self.DB_ENGINE.format(DB=dbname)
        self.db_engine = create_engine(engine_url, connect_args={'check_same_thread': False})
      
    def get_db_connection(self):
        return self.db_engine.connect()

    def create_db_tables(self):
        metadata = MetaData()
        StudentDetails = Table(STUDENTDETAILS, metadata,
            Column('usn', String, primary_key=True),
            Column('name', String, nullable=False),
            Column('semester', Integer, nullable=False),
            Column('branch', String, nullable=False),
            Column('section', String, nullable=False),
            Column('gpa', REAL, default=0.0),
        )

        StudentGrades = Table(STUDENTGRADES, metadata,
            Column('usn', String, ForeignKey('StudentDetails.usn'), primary_key=True ),
            Column('course', String, primary_key=True, nullable=False),
            Column('grade', String, default="Not announced")
        )
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    def select(self):
        connection = self.db_engine.connect()
        query =  "SELECT * FROM '{}';".format(STUDENTDETAILS)
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        print(ResultSet)

if __name__ == "__main__":
    db = MyDatabase("student.sqlite")
    db.create_db_tables()
