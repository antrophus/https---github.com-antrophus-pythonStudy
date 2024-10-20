#파일 읽기/쓰기
file_path = "C:\\javaStudy\\workspace_python\\Song.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("학교종이 땡땡땡\n")
    file.write("어서모이자\n")
    file.write("선생님이 우리를\n")
    file.write("기다리신다.")
