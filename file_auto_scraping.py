import os
from pathlib import Path

def collect_all_files(root_dir):
    """
    指定ディレクトリ配下の全ファイル情報を取得
    
    Args:
        root_dir: ルートディレクトリパス
    
    Returns:
        dict: ファイル情報の辞書
    """
    root_path = Path(root_dir)
    result = {
        "root_directory": str(root_path),
        "total_files": 0,
        "total_size": 0,
        "files": []
    }
    
    # 全ファイルを走査
    for file_path in root_path.rglob('*'):
        if file_path.is_file():
            try:
                # ファイル情報取得
                file_info = {
                    "path": str(file_path),
                    "relative_path": str(file_path.relative_to(root_path)),
                    "name": file_path.name,
                    "extension": file_path.suffix,
                    "size": file_path.stat().st_size,
                    "content": None
                }
                
                # テキストファイルの内容を読み込み
                if file_path.suffix in ['.py', '.txt', '.md', '.json', '.yml', '.yaml', '.toml', '.ini', '.cfg']:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            file_info["content"] = f.read()
                    except UnicodeDecodeError:
                        # UTF-8で読めない場合は他のエンコーディングを試す
                        try:
                            with open(file_path, 'r', encoding='shift-jis') as f:
                                file_info["content"] = f.read()
                        except:
                            file_info["content"] = "[バイナリファイルまたは読み込みエラー]"
                else:
                    file_info["content"] = "[バイナリファイル]"
                
                result["files"].append(file_info)
                result["total_files"] += 1
                result["total_size"] += file_info["size"]
                
            except Exception as e:
                print(f"エラー: {file_path} - {e}")
    
    return result


def save_to_markdown(data, output_file="directory_summary.md"):
    """
    取得したデータをMarkdown形式で保存
    
    Args:
        data: collect_all_files()の戻り値
        output_file: 出力ファイル名
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # ヘッダー
        f.write(f"# ディレクトリ構造とファイル内容\n\n")
        f.write(f"**ルートディレクトリ:** `{data['root_directory']}`\n\n")
        f.write(f"**総ファイル数:** {data['total_files']}\n\n")
        f.write(f"**合計サイズ:** {data['total_size']:,} bytes\n\n")
        f.write("---\n\n")
        
        # 各ファイル
        for file_info in data['files']:
            f.write(f"## {file_info['relative_path']}\n\n")
            f.write(f"- **サイズ:** {file_info['size']:,} bytes\n")
            f.write(f"- **拡張子:** `{file_info['extension']}`\n\n")
            
            if file_info['content'] and file_info['content'] != "[バイナリファイル]":
                f.write("### 内容:\n\n")
                f.write("```python\n" if file_info['extension'] == '.py' else "```\n")
                f.write(file_info['content'])
                f.write("\n```\n\n")
            else:
                f.write(f"*{file_info['content']}*\n\n")
            
            f.write("---\n\n")
    
    print(f"保存完了: {output_file}")


# 実行
if __name__ == "__main__":
    # ディレクトリパス
    target_dir = r"C:\Users\yukik\Desktop\python_programming"
    
    # データ取得
    print("ファイル情報を取得中...")
    data = collect_all_files(target_dir)
    
    # Markdown保存
    save_to_markdown(data, "python_programming_summary.md")
    
    # 簡易サマリー表示
    print(f"\n総ファイル数: {data['total_files']}")
    print(f"合計サイズ: {data['total_size']:,} bytes")
