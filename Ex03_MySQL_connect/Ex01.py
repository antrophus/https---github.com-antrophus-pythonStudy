#0.import
import mysql.connector
from mysql.connector import Error


try:
    #1.연결/컨넥션 얻기
    conn = mysql.connector.connect(
        host='localhost',        # 호스트
        user='phonebook',        # 사용자명
        password='phonebook',    # 비밀번호
        database='phonebook_db' # 데이터베이스명
    )

#2.커서생성
    cursor = conn.cursor()

#3.SQL문준비  / 바인딩 / 실행
    #--SQL문
    query ="""
        insert into person
        values(null, %s, %s, %s)
    """

    #--바인딩(튜플)
    data = ("홍길동","010-1232-9999", "02-2122-9999")

    #--실행
    cursor.execute(query, data) #임시반영
    conn.commit() #최종반영

#4.결과처리
    print(f'{cursor.rowcount}개 저장')

except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
#5.자원정리
    conn.close()
    cursor.close()



