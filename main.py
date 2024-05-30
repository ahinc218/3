import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def addFile(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write("")
        print(f"파일이 성공적으로 추가되었습니다: {file_path}")
    except Exception as e:
        print(f"파일 추가 중 오류가 발생했습니다: {e}")

def deleteFile(file_path):
    try:
        os.remove(file_path)
        print(f"파일이 성공적으로 삭제되었습니다: {file_path}")
    except Exception as e:
        print(f"파일 삭제 중 오류가 발생했습니다: {e}")

def createDirectory(dir_path):
    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"디렉토리가 성공적으로 생성되었습니다: {dir_path}")
    except Exception as e:
        print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")

def deleteDirectory(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"디렉토리가 성공적으로 삭제되었습니다: {dir_path}")
    except Exception as e:
        print(f"디렉토리 삭제 중 오류가 발생했습니다: {e}")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("실행 -> 파일 추가")
        file_path = input("추가할 파일의 경로를 입력하세요: ")
        addFile(file_path)

    elif func == "2":
        print("실행 -> 파일 삭제")
        file_path = input("삭제할 파일의 경로를 입력하세요: ")
        deleteFile(file_path)

    elif func == "3":
        print("기능 3 실행.")
        dir_path = input("생성할 디렉토리의 경로를 입력하세요: ")
        createDirectory(dir_path)

    elif func == "4":
        print("기능 4 실행.")
        dir_path = input("삭제할 디렉토리의 경로를 입력하세요: ")
        deleteDirectory(dir_path)

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사' 입력하여 파일 복사, '종료' 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")