import mysql.connector
from mysql.connector import Error

host="localhost"            # 호스트
user="phonebook"            # 사용자명
password="phonebook"        # 비밀번호
database="phonebook_db"      # 데이터베이스명

#get_connect() 함수
def get_connect():
    conn = mysql.connector.connect(
        host= host,
        user= user,
        password= password,
        database= database
    )
    return conn

# with ~ as ~ 문을 사용하면 close()를 사용할 필요가 없다. 
def add_person():
    try:
        with mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        ) as conn:
            
            #2.커서생성
            with conn.cursor() as cursor:

                #3.SQL문준비  / 바인딩 / 실행
                #--SQL문
                query = """
                    insert into person
                    values(null, %s, %s, %s)
                """

                #--바인딩(튜플)
                name = input("이름: ")
                hp = input("전화번호: ")
                company = input("회사: ")
                data = (name, hp, company)

                #--실행
                cursor.execute(query, data) #임시반영
                conn.commit() #최종반영

                print(f'{cursor.rowcount}개 저장')
    except Error as e:
        print(f"데이터베이스 오류: {e}")