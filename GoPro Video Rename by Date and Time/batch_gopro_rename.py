import os
import json
import shutil
from datetime import datetime
from tqdm import tqdm  # 引入 tqdm

# 獲取腳本所在的目錄
script_dir = os.path.dirname(os.path.abspath(__file__))

# 使用絕對路徑組合出 config.txt 的完整路徑
config_file_path = os.path.join(script_dir, "config.txt")

# 讀取 config.txt 中的設定
def read_config():
    with open(config_file_path, "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)
    return config_data

# 取得輸入和輸出資料夾路徑
config = read_config()
input_folder = config["input_folder"]
output_folder_name = config["output_folder"]

# 組合完整的輸出資料夾路徑
output_folder = os.path.join(os.path.dirname(__file__), output_folder_name)

# 確保輸出資料夾存在，如果不存在則創建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 列出目標資料夾中的所有MP4檔案
mp4_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mp4')]

# 使用 tqdm 來顯示進度條
for mp4_file in tqdm(mp4_files, desc="複製進度", unit="個"):
    source_file_path = os.path.join(input_folder, mp4_file)

    # 取得檔案的建立時間
    creation_time = datetime.fromtimestamp(os.path.getctime(source_file_path))

    # 格式化建立時間為指定的格式（例如：20200701_081245）
    formatted_time = creation_time.strftime('%Y%m%d_%H%M%S')

    # 建立新檔案名稱
    new_filename = formatted_time + '.mp4'

    # 建立新檔案的完整路徑
    new_file_path = os.path.join(output_folder, new_filename)

    # 複製檔案到輸出資料夾
    shutil.copy(source_file_path, new_file_path)

print('完成')