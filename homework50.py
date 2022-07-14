import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='vasif172',
    host='localhost',
    port='5432',
    database='vacansy_db'
)

cursor = connection.cursor()

# query = """
# CREATE TABLE jobs (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50) NOT NULL,
#     gain INT,
#     expiration_date DATE ,
#     lang BOOLEAN DEFAULT true,
#     city VARCHAR(30) NOT NULL
# )
# """



# query = """
# ALTER TABLE jobs DROP COLUMN city
# """
# 
# query = """
# ALTER TABLE jobs ADD COLUMN company VARCHAR(50);
# """
# 
# query = """
# ALTER TABLE jobs RENAME COLUMN gain TO salary
# """
# 
# query = """
# ALTER TABLE jobs ALTER COLUMN title TYPE VARCHAR(100);
# """

info_list = [
    # basliq, sirket, maas, bitme tarixi, xarici dil telebi
    ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
    ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
    ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
    ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
    ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
    ('Proqram təminatının testləşdirilməsi üzrə mühəndis',
     'ABB ASC', 1500, '2022-08-10', False),
    ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
    ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
    ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
    ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
    ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
    ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı',
     'ABB ASC', 2700, '2022-07-15', True),
    ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
    ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
    ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
    ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
    ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
    ('Proqram təminatı üzrə aparıcı mühəndis',
     'Kontakt Home', 2500, '2022-07-02', False),
    ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
    ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
    ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
    ('Cybersecurity Business Development Internship',
     'DEFSCOPE LLC', 2900, '2022-07-19', False),
    ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
]

# for melumat in info_list:
#     query = """
#     INSERT INTO jobs(title,company,salary,expiration_date,lang)
#     VALUES(%s,%s,%s,%s,%s)
#     """
#     cursor.execute(query,melumat)
#     connection.commit()

def show(cursor):
    print(*[desc[0].ljust(20) for desc in cursor.description])
    print('-'*20*8)
    print(*[''.join(str(z).ljust(25) for z in i) for i in cursor.fetchall()], sep='\n')

query = "SELECT * FROM jobs WHERE company = 'ABB ASC'"
query = "SELECT * FROM jobs WHERE company = 'ABB ASC' AND salary < 2000"
query = "SELECT * FROM jobs WHERE company = 'Kontakt Home' AND expiration_date < '2022-07-10'"
query = "SELECT * FROM jobs WHERE lang = FALSE AND salary > 2500"
query = "SELECT * FROM jobs WHERE title LIKE '%proqramçı'"
query = "SELECT * FROM jobs WHERE LOWER(title) NOT LIKE '%end'"
query = "SELECT * FROM jobs WHERE title ~'[İI]T'"
query = "SELECT * FROM jobs WHERE lang = TRUE ORDER BY salary DESC"
query = "SELECT MAX(salary) FROM jobs "
query = "SELECT * FROM jobs WHERE expiration_date > '2022-07-10' ORDER BY expiration_date DESC LIMIT 5 OFFSET 2"
# ------------------------ HOMEWORK 51 ------------------------------------
query = "UPDATE work SET salary = salary*1.15 WHERE salary<2000 AND exp_date>'2022-07-10';"
query = "DELETE FROM work WHERE company LIKE '%PHP%';"











cursor.execute(query)
# connection.commit()
show(cursor)






