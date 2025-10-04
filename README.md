# Python Programming ディレクトリ完全取得ツール

`C:\Users\hogehoge\Desktop\python_programming` 配下の全ファイルとその内容を綺麗に取得・整理するツールです。

---

## 機能

- ディレクトリツリー構造の可視化
- 全ファイルのメタデータ取得（サイズ、更新日時、行数）
- テキストファイルの内容取得
- Markdown形式の読みやすいレポート生成
- JSON形式のデータ出力

---

## インストール

### 必要な環境

- Python 3.7以上
- 標準ライブラリのみ使用（追加インストール不要）

### ファイルのダウンロード

```bash
# このリポジトリをクローン
git clone <repository-url>
cd python_programming_collector
```

---

## 使い方

### 基本的な使い方

```bash
python collect_files.py
```

### 出力ファイル

実行すると以下のファイルが生成されます：

```
python_programming_complete.md    # 読みやすいMarkdownレポート
python_programming_complete.json  # 機械可読なJSON形式データ
```

---

## 出力例

### Markdownレポート

```markdown
# Python Programming ディレクトリ完全レポート

## 概要

- **ルートディレクトリ:** `C:\Users\hogehoge\Desktop\python_programming`
- **総ファイル数:** 42
- **総ディレクトリ数:** 8
- **合計サイズ:** 156,789 bytes (0.15 MB)

## ディレクトリツリー

```
python_programming
├── module1
│   ├── __init__.py
│   └── main.py
├── module2
│   └── utils.py
└── tests
    └── test_main.py
```

## ファイル詳細

### module1/main.py

- **サイズ:** 2,345 bytes
- **行数:** 67

```python
def main():
    print("Hello, World!")
```
```

### JSONデータ

```json
{
  "metadata": {
    "root_directory": "C:\\Users\\hogehogek\\Desktop\\python_programming",
    "total_files": 42,
    "total_size": 156789
  },
  "files": [
    {
      "path": "...",
      "content": "...",
      "size": 2345,
      "lines": 67
    }
  ]
}
```

---

## カスタマイズ

### 特定のディレクトリを除外

`collect_files.py` を編集：

```python
# 除外するディレクトリパターン
EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'node_modules'}

def should_skip(path):
    return any(exclude in path.parts for exclude in EXCLUDE_DIRS)
```

### 特定の拡張子のみ取得

```python
# Pythonファイルのみ
TARGET_EXTENSIONS = {'.py'}

if item_path.suffix not in TARGET_EXTENSIONS:
    continue
```

### ファイルサイズ制限

```python
MAX_FILE_SIZE = 1024 * 1024  # 1MB

if file_size > MAX_FILE_SIZE:
    file_info["content"] = "[ファイルサイズが大きすぎます]"
```

---

## トラブルシューティング

### エラー: `UnicodeDecodeError`

**原因:** ファイルのエンコーディングが UTF-8 ではない

**解決策:** スクリプトは自動的に Shift-JIS も試します。それでもエラーが出る場合：

```python
# collect_files.py の該当箇所を修正
encodings = ['utf-8', 'shift-jis', 'cp932', 'latin-1']
for encoding in encodings:
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
        break
    except:
        continue
```

### エラー: `PermissionError`

**原因:** アクセス権限がない

**解決策:**
1. 管理者権限でPythonを実行
2. または、該当ファイル/ディレクトリを除外リストに追加

### 大量のファイルで処理が遅い

**解決策:** 並列処理版を使用

```python
from concurrent.futures import ThreadPoolExecutor

def collect_files_parallel(root_dir):
    with ThreadPoolExecutor(max_workers=4) as executor:
        # 並列処理実装
        pass
```

---

## スクリプト一覧

### 1. `collect_files.py` (基本版)

シンプルな完全取得スクリプト

```bash
python collect_files.py
```

### 2. `collect_files_advanced.py` (高度版)

- ツリー構造表示
- 統計情報
- カテゴリ別分類

```bash
python collect_files_advanced.py
```

### 3. `collect_python_only.py` (Python特化版)

Pythonファイルのみを取得

```bash
python collect_python_only.py
```

---

## 出力形式の選択

### Markdown形式（デフォルト）

```bash
python collect_files.py --format markdown
```

### JSON形式

```bash
python collect_files.py --format json
```

### HTML形式

```bash
python collect_files.py --format html
```

### テキスト形式

```bash
python collect_files.py --format text
```

---

## 詳細オプション

```bash
python collect_files.py --help
```

### オプション一覧

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--dir` | 対象ディレクトリ | カレントディレクトリ |
| `--output` | 出力ファイル名 | `report.md` |
| `--format` | 出力形式 | `markdown` |
| `--exclude` | 除外パターン | `.git,__pycache__` |
| `--max-size` | 最大ファイルサイズ(MB) | 無制限 |
| `--extensions` | 対象拡張子 | すべて |
| `--no-content` | 内容を含めない | False |
| `--tree-only` | ツリーのみ | False |

### 使用例

```bash
# Pythonファイルのみ、1MB以下
python collect_files.py --extensions .py --max-size 1

# テストディレクトリを除外
python collect_files.py --exclude "tests,__pycache__,.git"

# ツリー構造のみ表示
python collect_files.py --tree-only

# 複数ディレクトリを処理
python collect_files.py --dir "C:\Project1" "C:\Project2"
```

---

## ライセンス

MIT License

---

## 貢献

プルリクエスト歓迎

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

---

## よくある質問

### Q: バイナリファイルも取得できますか？

A: バイナリファイルのメタデータ（サイズ、パス等）は取得しますが、内容は `[バイナリファイル]` と表示されます。

### Q: 大きなプロジェクトでも使えますか？

A: はい。ただし、数千ファイル以上の場合は `--no-content` オプションでメタデータのみ取得することを推奨します。

### Q: 出力ファイルが文字化けします

A: 出力ファイルは UTF-8 で保存されます。メモ帳で開く場合は、エンコーディングを UTF-8 に指定してください。VS Code や PyCharm では自動認識されます。

---

## バージョン履歴

### v1.0.0 (2025-01-XX)
- 初回リリース
- 基本的なファイル取得機能
- Markdown/JSON出力

### v1.1.0 (予定)
- HTML出力対応
- 並列処理対応
- 進捗バー表示

---

## 関連ツール

- **tree** - ディレクトリツリー表示
- **fd** - 高速ファイル検索
- **ripgrep** - 高速grep

---

これで `C:\Users\hogehogek\Desktop\python_programming` の全データを綺麗に取得・整理できます。
