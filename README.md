# Zigzag SysMonitor CLI ⚡

**Zigzag SysMonitor CLI** adalah sebuah eksperimen kode yang mengubah skrip animasi "zigzag" klasik Python menjadi alat pemantauan sistem yang hidup, interaktif, dan estetis. Proyek ini dirancang untuk berjalan di terminal/command prompt sebagai widget minimalis yang memvisualisasikan "detak jantung" komputer Anda secara real-time.

## 📖 Tentang Proyek

Berbeda dengan animasi zigzag konvensional yang hanya mencetak karakter statis, alat ini terintegrasi langsung dengan perangkat keras Anda. Ia membaca data penggunaan CPU dan RAM, lalu menerjemahkannya ke dalam pola visual yang dinamis. Animasi ini juga dilengkapi dengan fisika gerakan berbasis gelombang sinus (sine wave), memberikan nuansa pergerakan yang luwes dan organik, tidak kaku seperti skrip aslinya.

## ✨ Fitur Unggulan

Proyek ini memiliki dua keunggulan utama. Pertama adalah **Visualisasi Berbasis Emoji**, di mana indikator beban kerja ditampilkan menggunakan metafora visual yang intuitif. Ikon akan berubah dari salju (❄️) saat CPU dingin, menjadi api (🔥) atau tengkorak (💀) saat beban kerja mencapai titik kritis, lengkap dengan data persentase RAM yang presisi. Kedua adalah **Interaktivitas Real-time**, yang memungkinkan pengguna mengendalikan kecepatan animasi secara langsung menggunakan keyboard tanpa perlu menghentikan program, memberikan kontrol penuh atas pengalaman visual yang ditampilkan.

## 🛠️ Prasyarat & Instalasi

Program ini dibangun menggunakan Python 3. Agar fitur pemantauan sistem dan interaksi keyboard berfungsi, Anda perlu menginstal dua pustaka eksternal.

Silakan jalankan perintah berikut di terminal Anda:

```bash
pip install psutil keyboard
```
## 🚀 Cara Penggunaan
Setelah pustaka terinstal, Anda cukup menjalankan skrip utama menggunakan Python. Pastikan terminal Anda mendukung encoding UTF-8 agar emoji dapat dirender dengan sempurna.

```bash

python main.py
```
(Ganti main.py dengan nama file skrip Anda)

## 🎮 Kontrol Keyboard
Saat program berjalan, Anda dapat menggunakan tombol berikut untuk berinteraksi:

Panah Atas (↑): Mempercepat animasi (mengurangi delay).

Panah Bawah (↓): Memperlambat animasi (menambah delay).

Esc: Keluar dari program dengan aman.

Dibuat dengan Python.
