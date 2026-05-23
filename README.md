# Description
このプロジェクトは、AIで完全に手放しでプログラムさせたらどうなる？のテストプロジェクトです。

## 指示プラン
Hermes Agent＋Free modelで作成。
ghコマンドだけ使えるようにして、あとは全権限を付与して、GitHub issueを活用しながら、Gitflowに則して作成させた。

# で、どうだった？
おおむね自動でやってくれたが、developブランチでコーディング->issueに対応したブランチ作成->ブランチからdevelopへのPRしようとしてコミット進んでおらずエラーしたところでスタック。
提案してきた修正方針も、リポジトリまっさらにしていい？という、強引な方法を提案。

もう少し頭の良いモデルを使えばこんなことないんだろうか。

---

# task-cli

コマンドラインで使えるシンプルなToDo管理ツール

## 機能

- `add <説明>` - タスクを追加
- `list` - タスク一覧を表示
- `done <ID>` - タスクを完了
- `delete <ID>` - タスクを削除

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/yoshikitaka/task-cli.git
cd task-cli

# 仮想環境を作成（推奨）
python3 -m venv venv
source venv/bin/activate

# インストール
pip install -e .
```

## 使い方

### タスクを追加

```bash
task-cli add "Hermesを試す"
# → タスクを追加しました: [1] Hermesを試す

# 期限付きタスク
task-cli add "レポートを提出" --due 2026-05-30
# → タスクを追加しました: [2] レポートを提出 (期限: 2026-05-30)
```

### タスク一覧を表示

```bash
task-cli list
# → 以下のように表示
# [1]  Hermesを試す
# [2] ✓ レポートを提出 (期限: 2026-05-30)
```

### タスクを完了

```bash
task-cli done 1
# → タスク [1] を完了しました。
```

### タスクを削除

```bash
task-cli delete 2
# → タスク [2] を削除しました。
```

## データ保存場所

タスクはプロジェクトルートの `tasks.json` に保存されます。

## 開発

### ブランチ戦略

このプロジェクトは **Gitflow** に従っています：

```
main      → 本番リリース用（安定版）
develop   → 開発統合ブランチ
feature/* → 機能開発ブランチ
release/* → リリース準備
hotfix/*  → 緊急修正
```

### Issue 駆動開発

1. GitHub Issue を作成
2. `feature/<issue番号>-<説明>` ブランチを作成
3. 機能を実装・コミット
4. `develop` へ PR を作成
5. レビュー・マージ後、Issue をクローズ

### ローカルでの開発

```bash
# developブランチから機能ブランチを作成
git checkout -b feature/3-filter-tasks develop

# 開発・コミット
git add .
git commit -m "feat: add filter option for list command (issue #3)"

# PRを作成
gh pr create --title "Add filter option for list command (issue #3)" --body "Closes #3" --base develop --head feature/3-filter-tasks
```

## コントリビューション

バグ報告や機能提案は GitHub Issues までお願いします。

## ライセンス

MIT License
