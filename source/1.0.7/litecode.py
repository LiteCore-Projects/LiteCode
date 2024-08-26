import time
import os
import re
import requests
import json
import glob
import platform
import signal
import urllib.request
import random
import sys
import subprocess
import locale
import shutil
from blessed import Terminal
from colorama import Fore, Back, Style, init
init(autoreset=True)
term = Terminal()
locale.setlocale(locale.LC_ALL, 'tr_TR.utf-8')
sys.setrecursionlimit(10000000)
os.system('cls')


loop = "false"
directory = os.getcwd()
first_directory = directory
variables = {
    'lc_version': '1.0.7',
    'i': '0',
    'term_startup': '0',
    'directory': directory,
    'cloud_dir': '0'
}
ifkosul = "false"
klasor = "0"
temp_file = "temp_" + str(random.randrange(1000, 10000)) + ".lc"

def terminal_boyutlarini_al():
    size = os.get_terminal_size()
    return size.columns, size.lines

def temp_dosyalari_sil():
    temp_dosyalar = glob.glob('temp_*.lc')
    
    for dosya in temp_dosyalar:
        try:
            os.remove(dosya)
        except Exception:
            pass

def cd(target_folder):
    try:
        os.chdir(target_folder)
        print("Changed to:", os.getcwd())
    except FileNotFoundError:
        print(f"Klasor '{target_folder}' mevcut degil.")




def handle_print_command(args):
    global variables
    argsdo()  # Replace variables in the arguments

    # Default colors
    text_color_code = Fore.RESET
    bg_color_code = Back.RESET

    # Extract color information from the text
    color_descriptors = re.findall(r'<(\w+)(?:\s+(\w+))?>', args)
    if color_descriptors:
        text_color = color_descriptors[0][0]
        bg_color = color_descriptors[0][1] if color_descriptors[0][1] else 'none'

        # Apply text color
        if text_color == 'red':
            text_color_code = Fore.RED
        elif text_color == 'blue':
            text_color_code = Fore.BLUE
        elif text_color == 'green':
            text_color_code = Fore.GREEN
        elif text_color == 'yellow':
            text_color_code = Fore.YELLOW
        elif text_color == 'black':
            text_color_code = Fore.BLACK
        elif text_color == 'white':
            text_color_code = Fore.WHITE
        elif text_color == 'cyan':
            text_color_code = Fore.CYAN
        elif text_color == 'magenta':
            text_color_code = Fore.MAGENTA

        # Apply background color
        if bg_color == 'none':
            bg_color_code = Back.RESET
        elif bg_color == 'red':
            bg_color_code = Back.RED
        elif bg_color == 'blue':
            bg_color_code = Back.BLUE
        elif bg_color == 'green':
            bg_color_code = Back.GREEN
        elif bg_color == 'yellow':
            bg_color_code = Back.YELLOW
        elif bg_color == 'black':
            bg_color_code = Back.BLACK
        elif bg_color == 'white':
            bg_color_code = Back.WHITE
        elif bg_color == 'cyan':
            bg_color_code = Back.CYAN
        elif bg_color == 'magenta':
            bg_color_code = Back.MAGENTA

    # Clean the text from color descriptors
    text = re.sub(r'<(\w+)(?:\s+(\w+))?>', '', args)

    # Print the text with formatting
    print(bg_color_code + text_color_code + text + Style.RESET_ALL)




def handle_insert_command(args):
    global variables
    argsdo()  # Replace variables in the arguments

    # Parse the arguments
    parts = args.split(" ")
    if len(parts) < 3:
        print("Error: Insufficient arguments for 'insert' command.")
        return
    
    x, y = int(parts[0]), int(parts[1])
    text = " ".join(parts[2:])

    # Default colors
    text_color_code = Fore.RESET
    bg_color_code = Back.RESET

    # Extract color information from the text
    color_descriptors = re.findall(r'<(\w+)(?:\s+(\w+))?>', text)
    if color_descriptors:
        text_color = color_descriptors[0][0]
        bg_color = color_descriptors[0][1] if color_descriptors[0][1] else 'none'

        # Apply text color
        if text_color == 'red':
            text_color_code = Fore.RED
        elif text_color == 'blue':
            text_color_code = Fore.BLUE
        elif text_color == 'green':
            text_color_code = Fore.GREEN
        elif text_color == 'yellow':
            text_color_code = Fore.YELLOW
        elif text_color == 'black':
            text_color_code = Fore.BLACK
        elif text_color == 'white':
            text_color_code = Fore.WHITE
        elif text_color == 'cyan':
            text_color_code = Fore.CYAN
        elif text_color == 'magenta':
            text_color_code = Fore.MAGENTA

        # Apply background color
        if bg_color == 'none':
            bg_color_code = Back.RESET
        elif bg_color == 'red':
            bg_color_code = Back.RED
        elif bg_color == 'blue':
            bg_color_code = Back.BLUE
        elif bg_color == 'green':
            bg_color_code = Back.GREEN
        elif bg_color == 'yellow':
            bg_color_code = Back.YELLOW
        elif bg_color == 'black':
            bg_color_code = Back.BLACK
        elif bg_color == 'white':
            bg_color_code = Back.WHITE
        elif bg_color == 'cyan':
            bg_color_code = Back.CYAN
        elif bg_color == 'magenta':
            bg_color_code = Back.MAGENTA

    # Clean the text from color descriptors
    text = re.sub(r'<(\w+)(?:\s+(\w+))?>', '', text)

    # Move cursor to the specified position and print the text with formatting
    sys.stdout.write(f"\033[{y};{x}H{bg_color_code}{text_color_code}{text}{Style.RESET_ALL}")
    sys.stdout.flush()



def argsdo():
    global variables, args
    degiskenler = re.findall(r"\$([a-zA-Z_]\w*)", args)
    for degisken in degiskenler:
        deger = variables.get(degisken, "null")
        args = args.replace(f"${degisken}", str(deger))

def terminal_boyutunu_ayarla(cols, lines):
    sistem = platform.system()
    if sistem == "Windows":
        os.system(f"mode con: cols={cols} lines={lines}")
    elif sistem in ["Linux", "Darwin"]:  # Darwin, macOS için
        os.system(f"printf '\\e[8;{lines};{cols}t'")
    else:
        raise NotImplementedError(f"{sistem} işletim sistemi desteklenmiyor.")

def setrunner(filename):
    global ffile, runner, readyrunner, temp_file
    ffile = filename
    runner = temp_file
    with open(ffile, 'r') as ffile:
        icerik = ffile.read()
    icerik = '\n'.join(
        line if '||' not in line else line.replace('||', '\n')
        for line in icerik.split('\n')
        if line.strip() and not line.strip().startswith('#')
    )
    with open(runner, 'w') as runner:
        runner.write(icerik)


def cumle_sozluk_olustur(cumle):
    parcalar = cumle.split(',')
    sozluk = {}
    for parca in parcalar:
        if ':' in parca:
            isim, deger = parca.split(':')
            sozluk[isim.strip()] = deger.strip()
    return sozluk


def satir_sayisi(dosya_adi):
    global variables
    try:
        with open(dosya_adi, 'r') as dosya:
            satir_sayisi = sum(1 for satir in dosya)
        return satir_sayisi
    except FileNotFoundError:
        return f"{dosya_adi} dosyası bulunamadı."
    except Exception as hata:
        return f"Hata oluştu: {hata}"


def calistir(dosya_yolu):
    try:
        if os.name == 'nt':
            subprocess.run(['start', 'cmd', '/k', f'call {dosya_yolu}'], shell=True)
        else:
            subprocess.run(['x-terminal-emulator', '-e', f'bash -c "source {dosya_yolu}"'], shell=True)
    except Exception as e:
        print(f"Hata oluştu: {e}")


def read(anahtar_yolu):
    global veri
    anahtarlar = anahtar_yolu.split()
    deger = veri.get(anahtarlar[0])
    for anahtar in anahtarlar[1:]:
        if deger is not None and anahtar in deger:
            deger = deger[anahtar]
        else:
            return None
    return deger


def oku(dosya_adi, satir_no):
    try:
        satir_no = int(satir_no)
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()
            if 1 <= satir_no <= len(satirlar):
                return satirlar[satir_no - 1].strip()
            else:
                return f"{dosya_adi} dosyasında {satir_no}. satır bulunmamaktadır."
    except FileNotFoundError:
        return f"{dosya_adi} dosyası bulunamadı."
    except ValueError:
        return "Lütfen geçerli bir satır numarası girin."

# * kordinat ile ekrana yazı yaz
def printxy(x, y, yazi):
    print(f"\033[{y};{x}H{yazi}")

def klasor_olustur(yol):
    try:
        os.makedirs(yol, exist_ok=True)
    except OSError as e:
        print(f"Hata: {e}")

temp_dosyalari_sil()
class litecode():
    def run(file):
        global args, variables, ifkosul, readyrunner, veri, temp_file
        directory = os.getcwd()
        variables['directory'] = directory
        columns, lines = terminal_boyutlarini_al()
        variables['term_col'] = columns
        variables['term_lin'] = lines
        setrunner(file)
        readyrunner = temp_file
        file = open(readyrunner, "r", encoding="utf-8")
        for satir in file:
            def ctrl_c_handler(signal, frame):
                print("\nCtrl+C tuş kombinasyonu algılandı. Program kapatılıyor.")
                file.close()
                #os.remove(temp_file) 
                exit(0)

            signal.signal(signal.SIGBREAK, ctrl_c_handler)
            signal.signal(signal.SIGINT, ctrl_c_handler)
            if satir.startswith("   ") or satir.startswith(" "):
                if not eval(ifkosul):
                    continue
            satir = satir.split()
            komut = satir[0]
            arg = satir[1:]
            args = " ".join(satir[1:])
            ttime = time.localtime()
            variables["time_sec"] = ttime.tm_sec
            variables["time_min"] = ttime.tm_min
            variables["time_hour"] = ttime.tm_hour
            variables["time_mday"] = ttime.tm_mday
            variables["time_mon"] = ttime.tm_mon
            variables["time_year"] = ttime.tm_year
            database_url = f"https://litecore-8ab53-default-rtdb.firebaseio.com/{variables['cloud_dir']}.json"
            database_secret = "JQB27aaS7gNEVToBB9gdydXRpfajWuZDPv7XJWG1"

            if komut in {"print", "echo", "write"}:
                argsdo()
                handle_print_command(args)
            elif komut == "insert":
                argsdo()
                handle_insert_command(args)
            elif komut == "run":
                if args == "":
                    print("Hata: (Run) eksik parametre!")
                else:
                    argsdo()
                    file.close()
                    litecode.run(args)
            elif komut == "wait":
                argsdo()
                time.sleep(int(args))
            elif komut == "set":
                argsdo()
                setarg = args.split("=")
                variables[setarg[0].strip()] = setarg[1].strip()
            elif komut == "if":
                cumle = args
                basina_eklenecek_harfler = "variables['"
                sonuna_eklenecek_harfler = "']"
                kelimeler = cumle.split()
                yeni_cumle = ""
                for kelime in kelimeler:
                    if kelime.startswith("$"):
                        yeni_cumle += basina_eklenecek_harfler + kelime[1:] + sonuna_eklenecek_harfler + " "
                    else:
                        if kelime not in {"not", "and", "or", "==", "!=", "<", ">", "<=", ">="}:
                            yeni_cumle += f'"{kelime}" '
                        else:
                            yeni_cumle += f'{kelime} '
                ifkosul = yeni_cumle.strip()
            elif komut == "math":
                argsdo()
                variables["math"] = eval(args)
            elif komut == "size":
                argsdo()
                arg = args.split(" ")
                terminal_boyutunu_ayarla(arg[0], arg[1])
            elif komut == "input":
                argsdo()
                inp = input(args)
                variables["input"] = inp
            elif komut == "split":
                spdegi = arg[0][1:]
                sp = variables[spdegi].split()
                for i in range(len(sp)):
                    variables[f"{spdegi}{i+1}"] = sp[i]
            elif komut in {"clear", "cls"}:
                os.system('cls')
            elif komut == "cd":
                argsdo()
                cd(args)
            elif komut == "loop":
                loop = args
                if args == "true":
                    loop_dir = os.getcwd()
            elif komut == "exit":
                temp_dosyalari_sil()
                #os.remove(temp_file)
                exit(0)
            elif komut == "random":
                args = f"{satir[1]} {satir[2]}"
                argsdo()
                rtemp = args.split()
                rand = random.randint(int(rtemp[0]), int(rtemp[1]))
                variables["random"] = rand
            elif komut == "delete":
                argsdo()
                os.remove(args)
            elif komut == "download":
                argsdo()
                arg = args.split()
                url = arg[0]
                hedef_dosya_yolu = arg[1]
                urllib.request.urlretrieve(url, hedef_dosya_yolu)
            elif komut == "read":
                argsdo()
                print(oku(arg[0], arg[1]))
            elif komut == "edit":
                argsdo()
                try:
                    with open(arg[0], "r", encoding="utf-8") as dosya:
                        satirlar = dosya.readlines()
                    satirlar[int(arg[1]) - 1] = f"{arg[2]}\n"
                    with open(arg[0], "w", encoding="utf-8") as dosya:
                        dosya.writelines(satirlar)
                except IndexError:
                    print("Geçersiz satır numarası.")
                except FileNotFoundError:
                    print(f"{arg[0]} dosyası bulunamadı.")
            elif komut == "del":
                argsdo()
                try:
                    with open(arg[0], "r", encoding="utf-8") as dosya:
                        satirlar = dosya.readlines()
                    satirlar.pop(int(arg[1]) - 1)
                    with open(arg[0], "w", encoding="utf-8") as dosya:
                        dosya.writelines(satirlar)
                except IndexError:
                    print("Geçersiz satır numarası.")
                except FileNotFoundError:
                    print(f"{arg[0]} dosyası bulunamadı.")
            elif komut == "dir":
                argsdo()
                print(os.listdir(args))
            elif komut == "send":
                try:
                    dosya_adi = arg[0]
                    hedef_dizin = arg[1] if len(arg) > 1 else ""
                    headers = {"Content-Type": "application/json; charset=UTF-8"}
                    with open(dosya_adi, "r", encoding="utf-8") as dosya:
                        veri = dosya.read()
                    veri_dict = {hedef_dizin: veri}
                    requests.patch(database_url, json=veri_dict, headers=headers)
                except Exception as hata:
                    print(f"Hata: {hata}")
            elif komut == "get":
                try:
                    dosya_adi = arg[0]
                    headers = {"Content-Type": "application/json; charset=UTF-8"}
                    response = requests.get(database_url, headers=headers)
                    if response.status_code == 200:
                        veri = response.json()
                        with open(dosya_adi, "w", encoding="utf-8") as dosya:
                            dosya.write(json.dumps(veri, indent=4))
                        print(f"{dosya_adi} başarıyla indirildi.")
                    else:
                        print(f"Hata: {response.status_code}")
                except Exception as hata:
                    print(f"Hata: {hata}")
            elif komut == "list":
                try:
                    headers = {"Content-Type": "application/json; charset=UTF-8"}
                    response = requests.get(database_url, headers=headers)
                    if response.status_code == 200:
                        veri = response.json()
                        print(json.dumps(veri, indent=4))
                    else:
                        print(f"Hata: {response.status_code}")
                except Exception as hata:
                    print(f"Hata: {hata}")
            else:
                print(f"'{komut}' komutu bulunamadı.")

if len(sys.argv) > 1:
    litecode.run(sys.argv[1])
else:
    print("Hata: Bir dosya adı belirtmelisiniz.") #litecode.run("litecode.lc")
