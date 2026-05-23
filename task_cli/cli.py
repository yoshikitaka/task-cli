#!/usr/bin/env python3
"""Task CLI - コマンドラインToDo管理ツール"""

import argparse
import sys
from .task import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Task CLI - シンプルなToDo管理")
    subparsers = parser.add_subparsers(dest="command", help="使用可能なコマンド")

    # add コマンド
    add_parser = subparsers.add_parser("add", help="タスクを追加")
    add_parser.add_argument("description", help="タスクの内容")
    add_parser.add_argument("--due", help="期限 (YYYY-MM-DD)")

    # list コマンド
    subparsers.add_parser("list", help="タスク一覧を表示")

    # done コマンド
    done_parser = subparsers.add_parser("done", help="タスクを完了")
    done_parser.add_argument("task_id", type=int, help="完了するタスクのID")

    # delete コマンド
    delete_parser = subparsers.add_parser("delete", help="タスクを削除")
    delete_parser.add_argument("task_id", type=int, help="削除するタスクのID")

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(args.description, args.due)
        print(f"タスクを追加しました: [{task.id}] {task.description}")
    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("タスクはありません。")
        else:
            for t in tasks:
                status = "✓" if t.done else " "
                due = f" (期限: {t.due})" if t.due else ""
                print(f"[{t.id}] {status} {t.description}{due}")
    elif args.command == "done":
        if manager.complete_task(args.task_id):
            print(f"タスク [{args.task_id}] を完了しました。")
        else:
            print(f"タスク [{args.task_id}] が見つかりません。")
            sys.exit(1)
    elif args.command == "delete":
        if manager.delete_task(args.task_id):
            print(f"タスク [{args.task_id}] を削除しました。")
        else:
            print(f"タスク [{args.task_id}] が見つかりません。")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
