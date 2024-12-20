# DoS-WiFi

**DoS-WiFi** adalah skrip Python yang dirancang untuk tujuan pendidikan, yang memungkinkan pengguna untuk melakukan serangan *Denial of Service* (DoS) pada jaringan Wi-Fi dengan menggunakan teknik deauthentication. Skrip ini menggunakan beberapa alat seperti `airodump-ng`, `airmon-ng`, dan `aireplay-ng` untuk mendeteksi jaringan Wi-Fi dan melakukan serangan terhadapnya.

> **Disclaimer:** Skrip ini hanya untuk tujuan pendidikan. Jangan digunakan untuk meretas atau menyerang jaringan yang tidak Anda miliki atau tidak memiliki izin untuk menguji.

## Fitur
- **Pemindaian Jaringan Wi-Fi**: Menampilkan semua jaringan Wi-Fi yang terdeteksi dalam jangkauan.
- **Pemilihan Jaringan untuk Serangan**: Pengguna dapat memilih jaringan Wi-Fi mana yang akan diserang.
- **Serangan Deauthentication**: Melakukan serangan deauthentication untuk memutuskan klien yang terhubung ke jaringan target.

## Prasyarat
Sebelum menjalankan skrip ini, pastikan Anda telah menginstal alat-alat berikut:
- `airodump-ng`
- `airmon-ng`
- `aireplay-ng`
- `iwconfig`
- `ip`
- `subprocess` (Modul Python standar)

Selain itu, skrip ini memerlukan hak akses superuser (sudo) untuk dapat memanipulasi adapter Wi-Fi.

## Cara Instalasi
1. **Clone Repositori**
   Clone repositori ini ke mesin Anda:
   ```bash
   git clone https://github.com/Cyberblaze-id/DoS-WiFi.git
   cd DoS-WiFi
2. Instalasi Dependensi Pastikan Anda memiliki dependensi yang dibutuhkan, seperti yang disebutkan pada bagian prasyarat. Biasanya, alat seperti aircrack-ng sudah ada dalam repositori distribusi Linux Anda.

3. Jalankan Skrip Setelah memastikan semuanya terpasang dengan benar, jalankan skrip ini dengan menggunakan sudo:
   ```bash
   sudo python3 DoS-WiFi.py

Penggunaan
1. Jalankan skrip menggunakan perintah sudo python3 DoS-WiFi.py.
2. Skrip akan memeriksa adapter Wi-Fi yang terhubung dan menampilkan daftar antarmuka yang tersedia.
3. Pilih antarmuka Wi-Fi yang ingin digunakan untuk serangan.
4. Skrip kemudian akan memasukkan adapter Wi-Fi ke mode monitor dan mulai memindai jaringan Wi-Fi di sekitar.
5. Pilih jaringan yang ingin diserang berdasarkan BSSID dan ESSID yang terdeteksi.
6. Skrip akan mengonfigurasi channel dan mulai melakukan serangan deauthentication pada jaringan yang dipilih.

Catatan
- Jangan menggunakan skrip ini pada jaringan yang bukan milik Anda. Melakukan serangan pada jaringan tanpa izin adalah ilegal dan dapat dikenakan hukuman pidana.
- Pastikan Anda memahami teknik ini dan tujuannya untuk tujuan pendidikan dan keamanan jaringan saja.
- 
Kontak
- GitHub: [Cyberblaze-id](https://github.com/Cyberblaze-id)
- Instagram: [@cyberblaze.id](https://www.instagram.com/cyberblaze.id/)
- YouTube: [Cyberblaze-id](https://www.youtube.com/@cyberblaze-id)
  
Lisensi
Skrip ini dibagikan di bawah lisensi pendidikan dan digunakan dengan tanggung jawab penuh oleh pengguna.

Pastikan kamu menyesuaikan URL atau informasi lainnya sesuai dengan yang kamu inginkan. File `README.md` ini memberikan penjelasan yang jelas dan rinci tentang cara menggunakan skrip kamu dan cara instalasi.

