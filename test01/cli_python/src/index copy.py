# 터미널 명령어를 쉽게 처리하게 도와주는 도구를 가져옴
import argparse

# cmd.py 파일에서 만든 기능들을 사용하려고 가져옴
from cmd import list, insert, update, remove

# 프로그램의 전체적인 설명을 설정함
parser = argparse.ArgumentParser(description="CLI 프로그램")

# 상세 명령어(list, insert 등)를 구분하기 위한 그룹을 만듦
# dest="command" : 입력된 명령어를 'command'라는 이름으로 저장하겠다는 뜻
subparsers = parser.add_subparsers(dest="command")

# --- 각 명령어(기능) 등록 과정 ---

# 1. 'list' 명령어 등록 → 추가로 입력할 내용 없음
add_parser = subparsers.add_parser("list")

# 2. 'insert' 명령어 등록
add_parser = subparsers.add_parser("insert")
# insert 뒤에 한 단어를 더 입력받도록 설정 → insert 단어1
add_parser.add_argument("word")

# 3. 'update' 명령어 등록
add_parser = subparsers.add_parser("update")
# update 뒤에 번호(id)와 바꿀 단어(word)를 순서대로 입력받음
add_parser.add_argument("id")
add_parser.add_argument("word")

# 4. 'delete' 명령어 등록
add_parser = subparsers.add_parser("delete")
# delete 뒤에 삭제할 번호(id)를 입력받음
add_parser.add_argument("id")

# 사용자가 입력한 모든 내용을 분석해서 args라는 변수에 담음
args = parser.parse_args()

# ---- 분석한 결과에 따라 실제 함수 실행 ----

# 1. list라고 쳤으면 목록 보여주기 실행
if args.command == "list": list()

# 2. insert라고 쳤으면 입력한 단어 추가하기 실행
if args.command == "insert": insert(args.word)

# 3. update라고 쳤으면 번호와 단어를 가지고 수정 실행
if args.command == "update": update(args.id, args.word)

# 4. delete라고 쳤으면 번호를 가지고 삭제 실행 → 코드상 remove 함수 호출
if args.command == "delete": remove(args.id)
