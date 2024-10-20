file_path = "C:\\javaStudy\\workspace_python\\PhoneDB.txt"

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

# 1. 전화번호 리스트 출력 함수
def load_phonebook():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            index = 1
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:  # 이름, 휴대전화, 회사전화번호
                    name = data[0]
                    hp = data[1]
                    company = data[2] 
                    print(f"{index}.\t{name}\t{hp}\t{company}")
                    index += 1
    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")

# 2. 전화번호 등록 함수 (기존 파일 덮어쓰기 방식)
def add_phonebook():
    try:
        # 기존 데이터를 리스트로 읽어오기
        phonebook = []
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    phonebook.append(line.strip())  # 기존 데이터 읽어와서 리스트에 저장
        except FileNotFoundError:
            pass  # 파일이 없을 경우 빈 리스트로 처리

        # 사용자로부터 데이터 입력받기
        name = input(">이름: ").strip()
        hp = input(">휴대전화: ").strip()
        company = input(">회사전화: ").strip()

        # 새 데이터를 추가
        new_person = f"{name}, {hp}, {company}"
        phonebook.append(new_person)  # 새 데이터를 리스트에 추가

        # 기존 데이터와 새 데이터를 포함하여 파일을 다시 작성 (덮어쓰기)
        with open(file_path, "w", encoding="utf-8") as file:
            for person in phonebook:
                file.write(person + "\n")  # 줄바꿈 포함하여 다시 파일에 기록

        print("[등록되었습니다.]")
    except Exception as e:
        print(f"등록 실패: {e}")

# 3. 전화번호 삭제 함수
def delete_phonebook():
    try:
        # 기존 데이터를 리스트에 임시 저장
        phonebook = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                phonebook.append(line.strip())

        if not phonebook:
            print("저장된 데이터가 없습니다.")
            return

        # 전화번호부 출력
        for index, entry in enumerate(phonebook, start=1):
            data = entry.split(',')
            name = data[0]
            hp = data[1]
            company = data[2]
            print(f"{index}.\t{name}\t{hp}\t{company}")

        # 삭제할 항목 선택
        del_no = int(input(">번호: "))

        if 1 <= del_no <= len(phonebook):
            del phonebook[del_no - 1]  # 선택한 항목 삭제
            with open(file_path, "w", encoding="utf-8") as file:  # 파일을 덮어쓰기 모드로 다시 씀
                for entry in phonebook:
                    file.write(entry + "\n")  # 각 데이터를 줄바꿈 처리하여 기록
            print("[삭제되었습니다.]")
        else:
            print("잘못된 번호입니다.")
    except Exception as e:
        print(f"삭제 실패: {e}")

# 4. 전화번호 검색 함수
def find_phonebook():
    try:
        search_name = input(">이름: ").strip()

        with open(file_path, "r", encoding="utf-8") as file:
            found = False
            index = 1
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                hp = data[1]
                company = data[2]
                if search_name in name:
                    print(f"{index}.\t{name}\t{hp}\t{company}")
                    found = True
                index += 1

            if not found:
                print("해당 이름을 가진 사람이 없습니다.")
    except Exception as e:
        print(f"검색 실패: {e}")
