import os
import pandas as pd
from sqlalchemy import create_engine

nilai_str = os.getenv("DATA_NILAI", "85,90,78,92,88")
nilai = list(map(int, nilai_str.split(',')))

df = pd.DataFrame({"Nilai": nilai})

print("Analisis Data Nilai Siswa")
print(f"Rata-rata Nilai: {df['Nilai'].mean()}")
print(f"Nilai Tertinggi: {df['Nilai'].max()}")
print(f"Nilai Terendah: {df['Nilai'].min()}")

os.makedirs('/app/output', exist_ok=True)
df.to_csv('/app/output/hasil_nilai.csv', index=False)

DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "analisis_db")

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
engine = create_engine(db_url)

df.to_sql("nilai_siswa", engine, if_exists="replace", index=False)

print("Data berhasil disimpan")