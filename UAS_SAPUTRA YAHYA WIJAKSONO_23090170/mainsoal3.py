import Soal_3

# Membuat instance dari AntrianRestoran
restoran = Soal_3.AntrianRestoran()

# Menambahkan pesanan ke dalam antrian
restoran.enqueue("Pesanan 1: Ayam Geprek")
restoran.enqueue("Pesanan 2: Omelet")
restoran.enqueue("Pesanan 3: Rica-Rica Pedas")

# Menampilkan antrian saat ini
restoran.tampilkan_antrian()

# Menghapus pesanan dari antrian
restoran.dequeue()
restoran.dequeue()

# Menampilkan antrian setelah penghapusan
restoran.tampilkan_antrian()

# Menghapus dari antrian yang kosong
restoran.dequeue()
restoran.dequeue()