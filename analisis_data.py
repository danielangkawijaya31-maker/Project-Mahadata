import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Membuat folder grafik jika belum ada
if not os.path.exists('grafik'):
    os.makedirs('grafik')

# 1. Membaca database menggunakan Pandas
conn = sqlite3.connect('database.db')
query = "SELECT * FROM penjualan_game"
df = pd.read_sql(query, conn)
conn.close()

print("--- 5 Baris Data Pertama ---")
print(df.head())
print("\n--- Ringkasan Statistik Data ---")
print(df.describe())

# 2. Pengolahan Data (Analisis Per Kategori Produk)
analisis_kategori = df.groupby('kategori_produk').agg({
    'jumlah_terjual': 'sum',
    'nilai_transaksi': 'mean'
}).reset_index()

print("\n--- Hasil Analisis Per Kategori Game ---")
print(analisis_kategori)

# 3. Visualisasi Data menggunakan Matplotlib
# Grafik Batang: Total Jumlah Terjual per Kategori
plt.figure(figsize=(9, 5))
plt.bar(analisis_kategori['kategori_produk'], analisis_kategori['jumlah_terjual'], color='royalblue')
plt.title('Total Jumlah Game & Aksesoris Terjual per Kategori')
plt.xlabel('Kategori Produk')
plt.ylabel('Total Terjual')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('grafik/bar_jumlah_game.png')
plt.close()

# Grafik Garis: Rata-rata Nilai Transaksi per Kategori
plt.figure(figsize=(9, 5))
plt.plot(analisis_kategori['kategori_produk'], analisis_kategori['nilai_transaksi'], marker='o', color='darkorange', linewidth=2.5)
plt.title('Rata-rata Nilai Transaksi per Kategori Produk')
plt.xlabel('Kategori Produk')
plt.ylabel('Rata-rata Nilai Transaksi')
plt.grid(True)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('grafik/line_nilai_game.png')
plt.close()

print("\nGrafik visualisasi berhasil disimpan di folder 'grafik/'!")

# 4. Ekspor Hasil ke Excel dan CSV
df.to_excel('hasil_export.xlsx', index=False)
df.to_csv('hasil_export.csv', index=False)

print("File ekspor 'hasil_export.xlsx' dan 'hasil_export.csv' berhasil dibuat!")