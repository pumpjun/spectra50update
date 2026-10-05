import os
import glob
import shutil
from cryptography.fernet import Fernet

# 대표님의 고유 비밀 키
SECRET_KEY = b'JlfkZ7Y3WRYU0nQ7kG_sEGRWWhyy0llLdtpYxYeis-I='
cipher = Fernet(SECRET_KEY)

# ★ 폴더 분리 설정 ★
source_folder = "real data"  # 원본 파일(엑셀, JSON, py)이 있는 폴더
output_folder = "data"       # 암호화된 파일(.enc)이 저장될 폴더

# 배포용 폴더(data)가 없으면 파이썬이 알아서 생성합니다.
os.makedirs(output_folder, exist_ok=True)

# --- 1. 엑셀 파일 암호화 ---
excel_files = glob.glob(os.path.join(source_folder, "*.xlsx"))
for file_path in excel_files:
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    enc_file_path = os.path.join(output_folder, f"{base_name}.enc")
    
    with open(file_path, "rb") as f:
        original_bytes = f.read()
        
    with open(enc_file_path, "wb") as f:
        f.write(cipher.encrypt(original_bytes))
    print(f"✅ 엑셀 암호화 완료: {enc_file_path}")

# --- 2. JSON 파일 암호화 ---
json_files = glob.glob(os.path.join(source_folder, "*.json"))
for file_path in json_files:
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    enc_file_path = os.path.join(output_folder, f"{base_name}.enc") 
    
    with open(file_path, "rb") as f:
        original_bytes = f.read()
        
    with open(enc_file_path, "wb") as f:
        f.write(cipher.encrypt(original_bytes))
    print(f"✅ JSON 암호화 완료: {enc_file_path}")

# --- 3. 파이썬(.py) 파일 암호화 ---
py_files = glob.glob(os.path.join(source_folder, "*.py"))
for file_path in py_files:
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    enc_file_path = os.path.join(output_folder, f"{base_name}.enc") 
    
    with open(file_path, "rb") as f:
        original_bytes = f.read()
        
    with open(enc_file_path, "wb") as f:
        f.write(cipher.encrypt(original_bytes))
    print(f"✅ 파이썬 코드 암호화 완료: {enc_file_path}")

print(f"🎉 모든 파일이 성공적으로 암호화되어 '{output_folder}' 폴더에 저장되었습니다!")

# --- 4. 자동 ZIP 압축 기능 추가 ---
target_dir = r"C:\Users\3F11\Desktop\암호화파일 만들기"
os.makedirs(target_dir, exist_ok=True)

zip_output_path = os.path.join(target_dir, "data")
shutil.make_archive(zip_output_path, 'zip', output_folder)

print(f"📦 압축 완료! 저장 경로: {target_dir}\\data.zip")