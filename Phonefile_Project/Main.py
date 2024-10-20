import Phone_dao as dao

def main():
    dao.title()
    while True:
        dao.menulist()
        try:
            no = int(input(">메뉴번호: "))
        except ValueError:
            print("메뉴 번호를 확인하세요")
            continue

        #1. 리스트
        if no == 1:
            print("<1.리스트>")
            dao.load_phonebook()
        # 2. 전화번호 등록
        elif no == 2:
            print("<2.등록>")
            dao.add_phonebook()
        # 3. 전화번호 삭제
        elif no == 3:
            print("<3.삭제>")
            dao.delete_phonebook()
        # 4. 전화번호 검색
        elif no == 4:
            dao.find_phonebook()
        # 5. 종료
        elif no == 5:
            dao.exit()
            break
        else:
            print("[다시 입력해 주세요.]")

if __name__ == "__main__":
    main()
