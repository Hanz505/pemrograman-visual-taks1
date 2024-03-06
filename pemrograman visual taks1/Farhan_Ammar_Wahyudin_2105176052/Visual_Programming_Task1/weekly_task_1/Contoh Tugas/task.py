class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print(f"Prodi: {self.prodi}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Tempat Tinggal: {self.tempat_tinggal}")
        print(f"Asal: {self.asal}")

# Buat objek baru dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Farhan Ammar Wahyudin", "B", "Pendidikan Komputer", "FKIP", "Tenggarong", "Kalimantan Tmur")

# Tampilkan informasi mahasiswa
mahasiswa1.tampilkan_info()


