from django.contrib import admin
from .models import Design

#↑モデルインポート。↓インポートしたモデルを管理サイトで扱う

admin.site.register(Design)


#管理サイトを使用する手順
"""
1. python3 manage.py createsuperuser コマンドを実行して、管理ユーザーを作る(IDとパスワード、メールアドレス(実在しないものでも可)を指定)
2. http://127.0.0.1:8000/admin/ にアクセスする。
3. 1のコマンドで作ったパスワードとIDを入力してログイン。
4. 任意のモデルを操作する(削除編集等可能。)
"""
