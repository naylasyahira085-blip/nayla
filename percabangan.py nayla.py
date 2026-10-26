# # input
# nilai = int(input("Masukkan Nilai: "))
# # proses
# if nilai >=80 and nilai <=100:
#     print("Anda Mendapatkan Nilai A")
# elif nilai >=70 and nilai <=80:
#     print("Anda Mendapatkan nilai B")
# elif nilai >=50 and nilai <=70:
#     print("Anda Mendapatkan nilai C")
# elif nilai >=30 and nilai <=50:
#     print("Anda Mendapatkan Nilai D")
# elif nilai >=0 and nilai <=20:
#     print("Andai Mendapatkan Nilai E")
# else:
#     print("Data Tidak Vald")




print("=====latihan=====")
#barang1
nama_barang= input("Masukkan Nama Barang:")
harga_barang= int(input("Masukkan Harga Barang:"))
#proses
if nama_barang.lower() == "kulkas":
    diskon = 0.10 *harga_barang
elif nama_barang.lower() == "tv":
    diskon = 0.5 * harga_barang 
elif nama_barang.lower() == "radio":
    diskon = 0
else:
    print("nama barang tidak tersedia")
    diskon = 0

jumlah_bayar = harga_barang - diskon

#output
print("=========================")
print("nama barang:",  nama_barang)
print("harga barang:", harga_barang)
print("diskon      :", diskon)
print("jumlah bayar:", jumlah_bayar)
print("===============")