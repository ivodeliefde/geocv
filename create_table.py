import psycopg2
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# create table
connection = psycopg2.connect(database=os.getenv("db_name"),user=os.getenv("db_username"),password=os.getenv("db_password"))

cursor = connection.cursor()
cursor.execute("CREATE DOMAIN category AS text CHECK (VALUE IN ('job', 'education'));")
cursor.execute("CREATE DOMAIN person AS text CHECK (VALUE IN ('Ivo de Liefde', 'Florian W. Fichtner'));")
cursor.execute("CREATE TABLE geocv (id SERIAL PRIMARY KEY,name person NOT NULL, title VARCHAR(255), cat category NOT NULL, starting_time DATE, end_time DATE, description VARCHAR(255), location GEOMETRY)")
connection.commit()

connection.close()
