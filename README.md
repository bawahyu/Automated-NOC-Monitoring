# Automated NOC Monitoring Tool 🚀

Proyek ini adalah sistem pemantauan infrastruktur jaringan otomatis yang dirancang untuk menggantikan penarikan log server secara manual. Dibangun untuk memastikan *uptime* operasional yang tinggi.

## 🛠️ Teknologi yang Digunakan
*   **Python 3:** Logika utama untuk menarik status jaringan dan memproses log error.
*   **Docker:** Containerisasi arsitektur agar dapat dijalankan di lingkungan server (OS) apa pun tanpa konflik dependensi.
*   **CSV/Excel Data Extraction:** Ekspor data otomatis untuk keperluan audit dan pelaporan (SIEM).

## 💡 Masalah yang Diselesaikan
Di lingkungan NOC tradisional, teknisi harus merefresh log secara manual untuk mendeteksi *downtime*. Skrip ini mengotomatisasi proses tersebut, mendeteksi anomali jaringan, dan langsung mencatatnya ke dalam arsip terstruktur.

## ⚙️ Fokus Arsitektur
Proyek ini mengimplementasikan konsep dasar Layer 7 dan Layer 3 pada OSI Model, memastikan inspeksi jaringan berjalan dengan presisi dan penggunaan memori yang ringan.
