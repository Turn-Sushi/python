
import argparse
from cmd import add, delete, wordList, ammend

parser = argparse.ArgumentParser(description="CLI 프로그램")
subparsers = parser.add_subparsers(dest="command")

# 단어 추가
add_parser = subparsers.add_parser("add", help="단어 추가")
add_parser.add_argument("word", help="단어 내용")

# 목록보기
list_parser = subparsers.add_parser("wordList", help="목록보기")

# 단어 삭제
delete_parser = subparsers.add_parser("delete", help="단어 삭제")
delete_parser.add_argument("id", type=int, help="단어 번호(id)")

# 단어 수정
ammend_parser = subparsers.add_parser("ammend", help="단어 수정")
ammend_parser.add_argument("id", type=int, help="단어 번호(id)")
ammend_parser.add_argument("word", help="단어 내용")


args = parser.parse_args()

if args.command == "add" :
    add(args.word)
elif args.command == "wordList" :
    wordList()
elif args.command == "delete" :
    delete(args.id)
elif args.command == "ammend" :
    ammend(args.id, args.word)