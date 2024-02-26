import os
import shutil

# 'Desktop' 폴더 경로 설정
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# 'icons' 폴더 경로 설정
icons_folder = os.path.join(desktop_path, 'icons')

# 'Downloads' 폴더 경로 설정
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# 'icons' 폴더 생성
if not os.path.exists(icons_folder):
    os.makedirs(icons_folder)
    print("아이콘 폴더를 생성했습니다.")

# 'Downloads' 폴더에서 모든 파일 목록 가져오기
download_files = os.listdir(downloads_folder)

# 'Downloads' 폴더에서 PNG 파일만 골라서 'icons' 폴더로 이동하고 이름 변경
for file in download_files:
    if file.endswith('.png'):
        old_path = os.path.join(downloads_folder, file)
        new_name = 'icon_' + file
        new_path = os.path.join(icons_folder, new_name)
        shutil.move(old_path, new_path)
        print(f"{file} 파일을 icons 폴더로 이동하고 {new_name}으로 이름을 변경했습니다.")

print("작업이 완료되었습니다.")
