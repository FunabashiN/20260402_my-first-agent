# load_env.py
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数を取得
api_key = os.getenv("OPENAI_API_KEY")

# キーの最初の5文字を表示
print(f"API_KEYの先頭: {api_key[:5]}...")
print("読み込み成功")