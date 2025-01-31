#0.import
import mysql.connector
from mysql.connector import Error

name = input("이름을 입력하세요: ")
hp = input("번호를 입력하세요: ")
company = input("회사번호 입력하셍: ")

try:
    #1.연결/컨넥션 얻기
    conn = mysql.connector.connect(
        host="localhost",
        user="phonebook",
        password="phonebook",
        database="phonebook_db"
    )
    print("연결 성공")

    #2.커서생성
    cursor = conn.cursor()

    #3.SQL문준비  / 바인딩 / 실행
    #--SQL문
    query ="""
        insert into person
        values(null, %s, %s, %s)
    """

    #--바인딩(튜플)
    data = (name, hp, company)

    #--실행
    cursor.execute(query, data) #임시반영
    conn.commit() #최종반영

    #4.결과처리
    print(f'{cursor.rowcount}개 저장')

except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
    #5.자원정리
    if conn is not None:
        conn.close()

    if cursor is not None:
        cursor.close()



