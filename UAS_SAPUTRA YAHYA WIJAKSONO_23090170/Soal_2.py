import pandas as pd

# Membuat DataFrame dari data yang diberikan
data = {
    'Nama': ['YAHYA', 'SALSA', 'SAIF'],
    'Algoritma Struktur Data 2': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}

df = pd.DataFrame(data)

# Menghitung rata-rata nilai untuk setiap mata kuliah
rata_rata_mata_kuliah = df[['Algoritma Struktur Data 2', 'Matematika Numerik']].mean()
print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_mata_kuliah)

# Menghitung rata-rata nilai untuk setiap mahasiswa
df['Rata-rata'] = df[['Algoritma Struktur Data 2', 'Matematika Numerik']].mean(axis=1)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df[['Nama', 'Rata-rata']])