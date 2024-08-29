import os
import sys
import shutil
import winreg
import requests
import zipfile
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    script = os.path.abspath(sys.argv[0])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)

def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def clean_folder(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        print(f"Kurulum klasörü temizlendi: {path}")

def download_file(url, destination):
    response = requests.get(url, stream=True)
    response.raise_for_status() 
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Dosya indirildi: {destination}")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"ZIP dosyası çıkarıldı: {extract_to}")

def copy_file_to_desktop(source_folder, file_name):
    desktop = os.path.join(os.environ.get('USERPROFILE'), 'Desktop')
    source_file = os.path.join(source_folder, file_name)
    dest_file = os.path.join(desktop, file_name)
    
    if os.path.exists(source_file):
        shutil.copy2(source_file, dest_file)
        print(f"{file_name} masaüstüne kopyalandı.")
    else:
        print(f"{file_name} bulunamadı.")

def register_file_type(app_name, destination_folder, file_extension=".lc"):
    try:
        zip_name = "litecode-release.zip" 
        zip_url = "https://github.com/LiteCore-Projects/LiteCode/raw/main/source/litecode-release.zip"  # GitHub indirme bağlantısı
        zip_path = os.path.join(destination_folder, zip_name)
        app_path = os.path.join(destination_folder, app_name)

        create_folder_if_not_exists(destination_folder)

        clean_folder(destination_folder)

        download_file(zip_url, zip_path)

        extract_zip(zip_path, destination_folder)

        os.remove(zip_path)

        # Dosya uzantısını ilişkilendir
        print("Dosya uzantısı kayıt ediliyor...")
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_extension)
        winreg.SetValue(key, "", winreg.REG_SZ, "LiteCodeFile")
        winreg.CloseKey(key)
        print(f"Dosya uzantısı {file_extension} ile ilişkilendirildi.")

        print("Dosya türü bilgileri ayarlanıyor...")
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, "LiteCodeFile")
        winreg.SetValue(key, "", winreg.REG_SZ, "LiteCode File")
        winreg.SetValue(key, "DefaultIcon", winreg.REG_SZ, f"{app_path},0")
        winreg.CloseKey(key)
        print("Dosya türü bilgileri ayarlandı.")

        print("Dosya türü ile ilişkilendirilen komutlar ayarlanıyor...")
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"LiteCodeFile\shell\open\command")
        winreg.SetValue(key, "", winreg.REG_SZ, f'"{app_path}" "%1"')
        winreg.CloseKey(key)
        print("Dosya türü ile ilişkilendirilen komutlar ayarlandı.")

        copy_file_to_desktop(destination_folder, "litecode.lc")

    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    if not is_admin():
        print("Kurulum yeni pencerede başlatılıyor..")
        run_as_admin()
        exit()
        return
        

    user_profile = os.environ.get('APPDATA')  # AppData\Roaming 
    if not user_profile:
        print("Kullanıcı profil yolu alınamadı.")
        sys.exit(1)

    destination_folder = os.path.join(user_profile, 'LiteCode')
    app_name = "litecode.exe"

    # Execute the installation logic
    register_file_type(app_name, destination_folder)

if __name__ == "__main__":
    print("litecode kurulum sihirbazı")
    print("-------------------------------------------------------------")
    print("kurulum başlatılıyor..")
    main()
    input("<enter to exit>")
