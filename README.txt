1. Download repository: git clone https://github.com/umialmuminati/resources-alert
2. Masuk ke direktori resources-alert
3. Buat satu direktori dengan nama log: mkdir log
4. Ubah file permission file change-mode.sh: chmod +x change-mode.sh
5. Jalankan file change-mode.sh: ./change-mode.sh
6. Ubah file permission file requirements-centos.sh (untuk CentOS) atau requirements-ubuntu.sh (untuk Ubuntu): chmod +x requirements-centos.sh atau chmod +x requirements-ubuntu.sh
7. Jalankan file requirements-centos.sh atau requirements-ubuntu.sh: ./requirements-centos.sh atau ./requirements-ubuntu.sh
8. Copy isi dari file supervisord.conf ke /etc/supervisord.conf, untuk ubuntu copy isi file ke /etc/supervisor/supervisord.conf
(SALIN ISI FILENYA SAJA JANGAN COPY FILENYA KARENA ISINYA BEDA, YANG DI GITHUB CUMA TAMBAHAN)
9. Untuk CentOS setelah langkah 7 jalankan command: systemctl enable supervisord dan systemctl start supervisord
10. Cek apakah supervisord sudah berjalan: systemctl status supervisord
Supervisor hanya digunakan untuk program cpu dan memory usage, untuk otomatisasi disk usage disini menggunakan cronjobs.<br> 
<h1>Berikut cara melakukan setup untuk cronjobs:</h1>
1. Konfigurasi cronjobs ada di file crontab.txt, salin isi dari file tersebut dan paste-kan di crontab
2. Caranya adalah dengan command: crontab -e
3. Kemudian tinggal di paste-kan saja.
