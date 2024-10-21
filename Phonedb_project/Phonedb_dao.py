import mysql.connector
from mysql.connector import Error

# 메뉴 타이틀 출력 함수
def title():
    print("*" * 50)
    print("*", " " * 11, "전화번호 관리 프로그램", " " * 11, "*")
    print("*" * 50)

# 메뉴 리스트 출력 함수
def menulist():
    print()
    print("1.리스트  ", " 2.등록  ", " 3.삭제  ", " 4.검색  ", " 5.종료 ")
    print("-" * 50)

# 종료 이미지 출력 함수
def exit():
    print("*" * 50)
    print("*", " " * 16, " 감사합니다.", " " * 16, "*")
    print("*" * 50)

#공통 인수
host="localhost"            # 호스트
user="phonebook"            # 사용자명
password="phonebook"        # 비밀번호
database="phonebook_db"      # 데이터베이스명


#1. 전화번호 리스트 출력 함수
def load_phonebook():
    try:
        #1. 연결/커넥션 얻기
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as conn:
            #2. 커서 생성
            with conn.cursor() as cursor:
                #3. SQL문 준비 / 바인딩 / 실행
                #--SQL문
                query = """
                    select person_id,
                            name,
                            hp,
                            company
                    from	person
                """
                #--바인딩(튜플)
                #--실행
                cursor.execute(query)
                #4. 쿼리 결과 받아오기
                resultset = cursor.fetchall()
                #5. 결과 출력
                person_list = []
                index = 1
                for row in resultset:
                    person_vo = {
                        "person_id": row[0],
                        "name": row[1],
                        "hp": row[2],
                        "company": row[3]
                    }
                    person_list.append(person_vo)
                    if len(person_vo) == 4:  # 이름, 휴대전화, 회사전화번호
                        name = person_vo["name"]
                        hp = person_vo["hp"]
                        company = person_vo["company"] 
                        print(f"{index}.\t{name}\t{hp}\t{company}")
                        index += 1
    except Error as e:
        print(f"데이터베이스 오류: {e}")


#2. 전화번호 등록 함수 
def add_person():
    name = input("이름을 입력하세요: ")
    hp = input("번호를 입력하세요: ")
    company = input("회사번호 입력하셍: ")
    try:
        #1. 연결/커넥션 얻기
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as conn:
            #2. 커서 생성
            with conn.cursor() as cursor:
                #3. SQL문 준비 / 바인딩 / 실행
                #--SQL문
                query = """
                    insert into person (name, hp, company)
                    values (%s, %s, %s)
                """
                #--바인딩(튜플)
                data = (name, hp, company) 
                #--실행
                cursor.execute(query, data) #임시 반영
                conn.commit()               #최종반영
                #4. 결과처리
                print(f'{cursor.rowcount}개 저장')
    except Error as e:
        print(f"데이터베이스 오류: {e}")


#3. 전화번호 삭제 함수
def delete_person():
    try:
        #1. 연결/커넥션 얻기
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as conn:
            #2. 커서 생성
            with conn.cursor() as cursor:
                #3. SQL문 준비 / 바인딩 / 실행
                query = """
                    select person_id,
                            name,
                            hp,
                            company
                    from	person
                """
                #--실행
                cursor.execute(query)
                #4. 쿼리 결과 받아오기
                resultset = cursor.fetchall()
                #5. 결과 출력
                person_list = []
                index = 1
                for row in resultset:
                    person_vo = {
                        "person_id": row[0],
                        "name": row[1],
                        "hp": row[2],
                        "company": row[3]
                    }
                    person_list.append(person_vo)
                    if len(person_vo) == 4:  # 이름, 휴대전화, 회사전화번호
                        name = person_vo["name"]
                        hp = person_vo["hp"]
                        company = person_vo["company"]
                        print(f"{index}.\t{name}\t{hp}\t{company}")
                        index += 1

                # 사용자가 인덱스 번호를 입력
                index_to_delete = int(input("삭제할 번호를 입력하세요: "))

                # 인덱스를 기반으로 person_id 추출
                if 1 <= index_to_delete <= len(person_list):
                    person_id = person_list[index_to_delete - 1]["person_id"]

                    #3. SQL문 준비 / 바인딩 / 실행
                    #--SQL문
                    query = """
                        delete from person
                        where person_id = %s
                    """
                    #--바인딩(튜플)
                    data = (person_id,)
                    #--실행
                    cursor.execute(query, data) #임시 반영
                    conn.commit()               #최종반영
                    #4. 결과처리
                    print(f'{cursor.rowcount}개 삭제')
                else:
                    print("잘못된 번호를 입력하셨습니다.")
                    
    except Error as e:
        print(f"데이터베이스 오류: {e}")
        
#4. 전화번호 검색 함수
'''
def search_person():
    try:
        search_name = input(">이름: ").strip()
        #1. 연결/커넥션 얻기
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as conn:
            #2. 커서 생성
            with conn.cursor() as cursor:
                #3. SQL문 준비 / 바인딩 / 실행
                query = """
                    select person_id,
                            name,
                            hp,
                            company
                    from    person
                """
                #--실행
                cursor.execute(query)
                #4. 쿼리 결과 받아오기
                resultset = cursor.fetchall()
                #5. 결과 출력
                person_list = []
                found = False
                index = 1
                for row in resultset:
                    person_vo = {
                        "person_id": row[0],
                        "name": row[1],
                        "hp": row[2],
                        "company": row[3]
                    }
                    person_list.append(person_vo)
                    if len(person_vo) == 4:  # 이름, 휴대전화, 회사전화번호
                        name = person_vo["name"]
                        hp = person_vo["hp"]
                        company = person_vo["company"]
                        if search_name in name:
                            print(f"{index}.\t{name}\t{hp}\t{company}")
                            found = True
                        index += 1
                if not found:
                    print("해당 이름을 가진 사람이 없습니다.")
    except Exception as e:
        print(f"검색 실패: {e}")
''' 
def search_person():
    try:
        search_name = input(">이름: ").strip()
        #1. 연결/커넥션 얻기
        with mysql.connector.connect(host=host, user=user, password=password, database=database) as conn:
            #2. 커서 생성
            with conn.cursor() as cursor:
                #3. SQL문 준비 / 바인딩 / 실행
                query = """
                    select person_id,
                            name,
                            hp,
                            company
                    from    person
                    where name like %s
                """
                #--바인딩(튜플)
                search_person = "%" + search_name + "%"  # 부분 일치 검색
                #--실행
                cursor.execute(query, (search_person,))
                #4. 쿼리 결과 받아오기
                resultset = cursor.fetchall()

                #5. 결과 출력
                if resultset:
                    index = 1
                    for row in resultset:
                        name = row[1]
                        hp = row[2]
                        company = row[3]
                        print(f"{index}.\t{name}\t{hp}\t{company}")
                        index += 1
                else:
                    print("해당 이름을 가진 사람이 없습니다.")
    except Exception as e:
        print(f"검색 실패: {e}")

