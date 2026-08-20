import subprocess
import platform
import csv
import time
from datetime import datetime
import socket

# ==========================================
# CONFIGURATION & CONSTANTS
# ==========================================
TARGET_NODES = [
    {"name": "Google_Core", "ip": "8.8.8.8"},
    {"name": "Cloudflare_Edge", "ip": "1.1.1.1"},
    {"name": "Internal_DB_Dummy", "ip": "192.0.2.254"}, # Pasti DOWN untuk tes
    {"name": "Local_Gateway", "ip": "127.0.0.1"}
]

LOG_FILE = "noc_audit_log.csv"

# Warna Terminal (ANSI Codes)
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ==========================================
# CORE ENGINE: NOC MONITOR
# ==========================================
class NOCMonitor:
    def __init__(self, targets, log_file):
        self.targets = targets
        self.log_file = log_file
        self.os_type = platform.system().lower()
        self._initialize_log()

    def _initialize_log(self):
        """Membuat header CSV jika file baru dijalankan."""
        try:
            with open(self.log_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                # Hanya tulis header jika file kosong (posisi kursor di 0)
                if file.tell() == 0:
                    writer.writerow(["TIMESTAMP", "NODE_NAME", "IP_ADDRESS", "STATUS", "RESOLUTION"])
        except PermissionError:
            print(f"{RED}[FATAL ERROR] Tutup file {self.log_file} di Excel sebelum menjalankan sistem!{RESET}")
            exit(1)

    def ping_node(self, ip):
        """Mengeksekusi ICMP Request ke node target lintas OS (Windows/Linux)."""
        if self.os_type == 'windows':
            # -n: count, -w: timeout dalam milidetik
            command = ['ping', '-n', '1', '-w', '1000', ip]
        else:
            # Linux: -c: count, -W: timeout dalam detik
            command = ['ping', '-c', '1', '-W', '1', ip]
        
        try:
            # DEVNULL digunakan agar output ping bawaan OS tidak mengotori layar
            response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            return response == 0
        except Exception:
            return False

    def run_audit(self):
        """Menjalankan siklus audit jaringan."""
        print(f"{YELLOW}>>> INITIATING AUTOMATED NETWORK AUDIT...{RESET}")
        print(f"Target Nodes : {len(self.targets)} Hosts")
        print(f"Log Output   : {self.log_file}")
        print("-" * 60)
        
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            for node in self.targets:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                is_up = self.ping_node(node['ip'])
                
                if is_up:
                    status_log = "UP"
                    print(f"[{timestamp}] {GREEN}[OK]{RESET} {node['name']:<18} ({node['ip']:<12}) -> LINK ESTABLISHED")
                else:
                    status_log = "DOWN"
                    print(f"[{timestamp}] {RED}[!!]{RESET} {node['name']:<18} ({node['ip']:<12}) -> CONNECTION TIMEOUT")
                
                # Catat ke sistem forensik (CSV)
                writer.writerow([timestamp, node['name'], node['ip'], status_log, "AUTO-AUDIT"])
                file.flush()
                
        print("-" * 60)

# ==========================================
# EXECUTION (MAIN LOOP)
# ==========================================
if __name__ == "__main__":
    monitor = NOCMonitor(TARGET_NODES, LOG_FILE)
    
    print(f"\n{YELLOW}================================================={RESET}")
    print(f"{YELLOW}  ENTERPRISE NOC - AUTOMATED MONITORING SYSTEM   {RESET}")
    print(f"{YELLOW}================================================={RESET}")
    print("Tekan CTRL+C untuk mematikan engine.\n")
    
    try:
        while True:
            monitor.run_audit()
            time.sleep(10) # Delay 10 detik per siklus untuk mencegah spam jaringan
    except KeyboardInterrupt:
        print(f"\n{RED}[SYSTEM HALTED]{RESET} Manual interrupt diterima. Audit dihentikan.")