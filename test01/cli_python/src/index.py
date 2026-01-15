import argparse
from cmd import list, insert, update, remove

parser = argparse.ArgumentParser(description="CLI 프로그램")
subparsers = parser.add_subparsers(dest="command")

list_parser = subparsers.add_parser("list")

insert_parser = subparsers.add_parser("insert")
insert_parser.add_argument("word")

update_parser = subparsers.add_parser("update")
update_parser.add_argument("id")
update_parser.add_argument("word")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id")


args = parser.parse_args()


if args.command == "list" : list()
if args.command == "insert" : insert(args.word)
if args.command == "update" : update(args.id, args.word)
if args.command == "delete" : remove(args.id)


