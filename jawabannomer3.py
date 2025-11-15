class RekeningBank:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.saldo = saldo_awal

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setor {jumlah} berhasil. Saldo sekarang: {self.saldo}")
        else:
            print("Jumlah setor tidak valid.")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup!")
        elif jumlah <= 0:
            print("Jumlah tarik tidak valid.")
        else:
            self.saldo -= jumlah
            print(f"Tarik {jumlah} berhasil. Saldo sekarang: {self.saldo}")

    def info(self):
        print(f"Pemilik: {self.pemilik} | Saldo: {self.saldo}")


class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis
        self.jumlah = jumlah

    def tampilkan(self):
        print(f"Transaksi: {self.jenis} sebesar {self.jumlah}")


class Bank:
    def __init__(self, nama_bank):
        self.nama_bank = nama_bank
        self.daftar_rekening = []

    def tambahRekening(self, rekening):
        self.daftar_rekening.append(rekening)
        print(f"Rekening {rekening.pemilik} ditambahkan ke {self.nama_bank}")

    def tampilkanSemua(self):
        print(f"Daftar Rekening di {self.nama_bank}:")
        for r in self.daftar_rekening:
            r.info()


r1 = RekeningBank("Budi", 100000)
r1.info()
r1.setor(50000)
r1.tarik(200000)
r1.tarik(30000)
r1.info()


bank = Bank("Bank Aman Sejahtera")
bank.tambahRekening(r1)
bank.tampilkanSemua()

t1 = Transaksi("Setor", 50000)
t1.tampilkan()
