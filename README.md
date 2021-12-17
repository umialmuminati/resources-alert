# Langkah untuk menggunakan resources-alert
<ol type = "1">
  <li>Download repository: git clone https://github.com/umialmuminati/resources-alert</li>
  <li>Masuk ke direktori resources-alert</li>
  <li>Buat satu direktori dengan nama log: mkdir log</li>
  <li>Ubah file permission file change-mode.sh: chmod +x change-mode.sh</li>
  <li>Jalankan file change-mode.sh: ./change-mode.sh</li>
  <li>Ubah file permission file requirements-centos.sh (untuk CentOS) atau requirements-ubuntu.sh (untuk Ubuntu) menggunakan command chmod +x</li>
  <li>Jalankan file requirements-centos.sh atau requirements-ubuntu.sh: ./requirements-centos.sh atau ./requirements-ubuntu.sh</li>
  <li>Copy isi dari file supervisord.conf ke /etc/supervisord.conf, untuk ubuntu copy isi file ke /etc/supervisor/supervisord.conf</li>
  <b>(SALIN ISI FILENYA SAJA JANGAN COPY FILENYA KARENA ISINYA BEDA, YANG DI GITHUB CUMA TAMBAHAN)</b>
  <li>Untuk CentOS setelah langkah 7 jalankan command: systemctl enable supervisord dan systemctl start supervisord</li>
  <li>Cek apakah supervisord sudah berjalan: systemctl status supervisord</li>
</ol>

<b> note: Supervisor hanya digunakan untuk program cpu dan memory usage, untuk otomatisasi disk usage disini menggunakan cronjobs. </b>
# Berikut cara melakukan setup untuk cronjobs:
<ol type = "1">
  <li>Konfigurasi cronjobs ada di file crontab.txt, salin isi dari file tersebut dan paste-kan di crontab</li>
  <li>Caranya adalah dengan command: crontab -e</li>
  <li>Kemudian tinggal di paste-kan saja.</li>
</ol>
<h1> Creator </h1>
&#10084; Umi Al Mu'minati
