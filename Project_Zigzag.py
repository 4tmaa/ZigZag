import time
import sys
import math
import psutil
import keyboard

# Memastikan terminal menggunakan encoding UTF-8 agar emoji muncul
sys.stdout.reconfigure(encoding='utf-8')

print("Tekan 'Esc' untuk keluar.")
print("Tekan 'Panah Atas' untuk mempercepat, 'Panah Bawah' untuk memperlambat.")

indent = 0
indent_increasing = True
base_speed = 0.05

# Daftar Emoji berdasarkan level stress CPU
emoji_levels = ['❄️', '🍃', '⚡', '🔥', '💀']

try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nProgram dihentikan oleh Pengguna.")
            sys.exit()
        if keyboard.is_pressed('up'):
            base_speed = max(0.01, base_speed - 0.005)
        if keyboard.is_pressed('down'):
            base_speed = min(0.2, base_speed + 0.005)

        # Mengambil data CPU dan RAM
        cpu_usage = psutil.cpu_percent(interval=None)
        ram_info = psutil.virtual_memory()
        ram_usage = ram_info.percent
        
        # Visualisasi Emoji tetap mengikuti CPU (karena lebih dinamis)
        num_icons = int((cpu_usage / 100) * 10) + 1
        idx = min(4, int(cpu_usage / 20)) 
        selected_icon = emoji_levels[idx]

        # Membentuk pola visual dengan label lengkap
        # Format: [Emoji] CPU: ..% | RAM: ..%
        visual_pattern = f"{selected_icon * num_icons} CPU: {cpu_usage}% | RAM: {ram_usage}%"

        print(' ' * indent + visual_pattern)

        # Fisika gerakan
        swing_factor = math.sin((indent / 20) * math.pi)
        dynamic_delay = base_speed + (0.03 * (1 - swing_factor))
        
        time.sleep(dynamic_delay)

        if indent_increasing:
            indent += 1
            if indent >= 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent <= 0:
                indent_increasing = True

except Exception as e:
    print(f"\nTerjadi kesalahan: {e}")