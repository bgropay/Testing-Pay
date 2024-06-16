#!/usr/bin/env python3
# ******************************************************* #
# * [+] Program   : PyUnzip                             * #
# * [+] Pembuat   : BgRopay                             * #
# * [+] Deskripsi : Crack Kata Sandi File Zip           * #
# * [+] Github    : https://github.com/bgropay/pyunzip  * #
# ******************************************************* #
# * Maaf ya Bro SC (Source Code) nya GW encrypt soalnya * #
# * takut di copy sama oknum PLAGIATOR (seseorang       * #
# * yang melakukan tindakan plagiat, yaitu mengambil,   * #
# * menyalin, atau menggunakan karya orang lain tanpa   * #
# * izin atau persetujuan, serta tanpa memberikan       * #
# * pengakuan atau kredit kepada pencipta aslinya.)     * #
# ******************************************************* #

import os
import time
import getpass
try:
    import colorama
except ImportError:
    print("Terjadi kesalahan: Modul colorama belum terinstal. Instal dengan mengetikan perintah 'pip3 install colorama'.")
    exit(1)
try:
    import pyzipper
except ImportError:
    print("Terjadi kesalahan: Modul pyzipper belum terinstal. Instal dengan mengetikan perintah 'pip3 install pyzipper'.")
    exit(1)

# mengubah output warna teks
m = colorama.Fore.LIGHTRED_EX    # merah
h = colorama.Fore.LIGHTGREEN_EX  # hijau
b = colorama.Fore.LIGHTBLUE_EX   # biru
k = colorama.Fore.LIGHTYELLOW_EX # kuning
c = colorama.Fore.LIGHTCYAN_EX   # cyan
p = colorama.Fore.LIGHTWHITE_EX  # putih
r = colorama.Fore.RESET          # reset

# password untuk login
password = "kunyuk is here"

# mengecek jenis sistem operasi
so = os.name

# sistem operasi windows 
if so == "nt":
    # membersihkan layar terminal windows
    os.system("cls")
# sistem operasi linux
elif so == "posix":
    # membersihkan layar terminal linux
    os.system("clear")
else:
    print(f"{m}[-] {p}Sistem operasi Anda tidak mendukung untuk menjalankan program PyUnzip :({r}")
    exit(1)

# ************** INPUT PASSWORD **************
while True:
    try:
        input_password = getpass.getpass(prompt=f"{c}[»] {p}Password: ")
        if input_password != password:
            print(f"{m}[-] {p}Password salah. Silahkan coba lagi.{r}")
            continue
        else:
            print(f"{h}[+] {p}Password benar.{r}")
            time.sleep(3)
            break
    except KeyboardInterrupt:
        print(f"\n{m}[-] {p}Keluar...{k}:({r}")
        exit(1)

# mengecek jenis sistem operasi
so = os.name

# sistem operasi windows 
if so == "nt":
    # membersihkan layar terminal windows
    os.system("cls")
# sistem operasi linux
elif so == "posix":
    # membersihkan layar terminal linux
    os.system("clear")
else:
    print(f"{m}[-] {p}Sistem operasi Anda tidak mendukung untuk menjalankan program PyUnzip :({r}")
    exit(1)
    
# Mlmenampilkan banner
print(f"""
{p}--------------------------------------------------{r}
{h}+                                                +{r}
   {b}[*]           {p}Program: {k}pyunzip           {b}[*]{r}
   {b}[*]            {p}Pembuat: {k}Ropay            {b}[*]{r}
   {b}[*]  {p}Github: {k}github.com/bgropay/pyunzip  {b}[*]{r}
{h}+                                                +{r}
{p}--------------------------------------------------{r}
""")

# ************** INPUT FILE ZIP **************
while True:
    try:
        input_zip = input(f"{c}[»] {p}Masukkan jalur ke file Zip: {c}")
        if not os.path.isfile(input_zip):
            print(f"{m}[-] {p}File Zip {input_zip} tidak ditemukan.{r}")
            continue
        if not input_zip.endswith(".zip"):
            print(f"{m}[-] {p}File {input_zip} bukan file Zip.{r}")
            continue
        print(f"{h}[+] {p}File Zip {input_zip} ditemukan.{r}")
        break
    except KeyboardInterrupt:
        print(f"\n{m}[-] {p}Keluar...{k}:({r}")
        exit(1)

# ************** INPUT FILE WORDLIST **************
while True:
    try:
        input_wordlist = input(f"{c}[»] {p}Masukkan jalur ke file Wordlist: {c}")
        if not os.path.isfile(input_wordlist):
            print(f"{m}[-] {p}File Wordlist {input_wordlist} tidak ditemukan.{r}")
            continue
        print(f"{h}[+] {p}File Wordlist {input_wordlist} ditemukan.{r}")

        print(f"{b}[*] {p}Menghitung jumlah kata sandi yang terdapat dalam file Wordlist {input_wordlist}...{r}")
        time.sleep(3)
        with open(input_wordlist, "r", encoding="latin-1", errors="ignore") as list_kata_sandi:
            jumlah_kata_sandi = sum(1 for baris in list_kata_sandi)
        print(f"{h}[+] {p}Jumlah kata sandi yang terdapat dalam file {h}{input_wordlist} {p}sebanyak: {h}{jumlah_kata_sandi} {p}kata sandi.{r}\n")
        time.sleep(3)
        break
    except KeyboardInterrupt:
        print(f"\n{m}[-] {p}Keluar...{k}:({r}")
        exit(1)

# ************** CRACK KATA SANDI FILE ZIP **************
found_password = False

try:
    with pyzipper.AESZipFile(input_zip) as fz:
        with open(input_wordlist, encoding="latin-1", errors="ignore") as fw:
            for baris_file in fw:
                # kata sandi
                kata_sandi = baris_file.strip()
                try:
                    fz.pwd = kata_sandi.encode()
                     # kondisi kata sandi file zip ditemukan
                    if fz.testzip() is None:
                        print(f"{p}--------------------------------------------------{r}")
                        print(f"{h}[+] {p}Kata sandi ditemukan: {h}{kata_sandi}{r}")
                        print(f"{p}--------------------------------------------------{r}")
                        found_password = True
                        exit(0)
                # pengecualian KeyboardInterrupt
                except KeyboardInterrupt:
                    print(f"\n{m}[-] {p}Keluar...{k}:({r}")
                    exit(1)
                except Exception:  # pengecualian
                    print(f"{m}[-] {p}Kata sandi salah: {m}{kata_sandi}{r}")
                    continue
    # kondisi kata sandi file zip tidak ditemukan
    if not found_password:
        print(f"{p}--------------------------------------------------{r}")
        print(f"{m}[-] {p}Kata sandi tidak ditemukan dalam file wordlist {m}{input_wordlist}{r}")
        print(f"{p}--------------------------------------------------{r}")
except Exception as e:
    print(f"{m}[-] {p}Kesalahan terjadi: {m}{e}{r}")
