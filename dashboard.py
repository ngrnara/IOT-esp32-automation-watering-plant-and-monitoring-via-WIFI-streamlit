import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(
    page_title="Monitor Tanaman Pintar",
    page_icon="🌱",
    layout="wide"
)

# ================= JUDUL DASHBOARD =================
st.title("🌱 Smart Farming Monitor: Project Tani")
st.markdown("Dashboard monitoring kelembapan tanah dan kontrol pompa otomatis berbasis IoT (ESP32).")

# ================= FUNGSI AMBIL DATA =================
# Ini URL KHUSUS untuk download data kamu sebagai CSV (Update otomatis)
SHEET_ID = "1kcC4SIEI01crLUapKUeudslCWXp-X5xbTg3BGlJUMrw"
SHEET_GID = "0" # ID Tab kamu
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={SHEET_GID}"

def get_data():
    try:
        # Baca data dari Google Sheets
        df = pd.read_csv(CSV_URL)
        
        # Pastikan nama kolom sesuai (Hapus spasi di nama kolom jika ada)
        df.columns = df.columns.str.strip()
        
        return df
    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")
        return pd.DataFrame()

# ================= AUTO REFRESH LOGIC =================
# Wadah kosong untuk menampung isi dashboard
placeholder = st.empty()

# Loop supaya data update terus tiap detik
while True:
    df = get_data()

    if not df.empty:
        # Ambil data baris paling bawah (Terbaru)
        last_row = df.iloc[-1]
        
        # Ambil nilai-nilai penting
        waktu_terakhir = last_row['Waktu']
        kelembapan = int(last_row['Kelembapan'])
        status_pompa = last_row['Status']
        
        # Hitung Total Durasi Nyala Hari Ini (Opsional)
        # Menjumlahkan kolom 'Durasi'
        total_air = df['Durasi'].sum() 

        with placeholder.container():
            # --- BARIS 1: KARTU INDIKATOR (METRICS) ---
            k1, k2, k3, k4 = st.columns(4)
            
            with k1:
                st.metric(label="🕒 Update Terakhir", value=waktu_terakhir.split(" ")[1]) # Ambil jamnya aja
            
            with k2:
                # Warna dinamis: Kalau kering ( > 3000) jadi merah
                delta_color = "inverse" if kelembapan > 3000 else "normal"
                st.metric(label="💧 Kelembapan Tanah", value=f"{kelembapan}", delta="Batas Basah < 2900", delta_color="off")

            with k3:
                # Status Pompa
                icon = "💦 MENYIRAM" if status_pompa == "ON" else "✅ STANDBY"
                st.metric(label="⚙️ Status Pompa", value=icon)

            with k4:
                st.metric(label="⏱️ Total Durasi Siram", value=f"{total_air} Detik")

            # --- BARIS 2: GRAFIK ---
            col_grafik1, col_grafik2 = st.columns(2)

            with col_grafik1:
                st.subheader("📈 Grafik Kelembapan Real-time")
                # Ambil 50 data terakhir saja biar grafik gak berat
                fig_line = px.line(df.tail(50), x='Waktu', y='Kelembapan', markers=True, title='Tren Kelembapan (50 Data Terakhir)')
                # Tambah garis batas merah (Kering) dan hijau (Basah)
                fig_line.add_hline(y=3600, line_dash="dash", line_color="red", annotation_text="Batas Kering")
                fig_line.add_hline(y=2900, line_dash="dash", line_color="green", annotation_text="Batas Basah")
                st.plotly_chart(fig_line, use_container_width=True, key=f"grafik_satu_{time.time()}")

            with col_grafik2:
                st.subheader("📊 Riwayat Aktivitas Pompa")
                # Filter hanya saat pompa ON/OFF saja
                df_pompa = df[df['Durasi'] > 0]
                if not df_pompa.empty:
                    fig_bar = px.bar(df_pompa.tail(10), x='Waktu', y='Durasi', color='Durasi', title='10 Aktivitas Penyiraman Terakhir')
                    st.plotly_chart(fig_bar, use_container_width=True, key=f"grafik_dua_{time.time()}")
                else:
                    st.info("Belum ada aktivitas penyiraman yang tercatat.")

            # --- BARIS 3: DATA MENTAH (Tabel) ---
            with st.expander("Lihat Data Mentah (Tabel Excel)"):
                st.dataframe(df.sort_index(ascending=False)) # Tampilkan dari yang paling baru

        # Tunggu 2 detik sebelum refresh lagi
        time.sleep(2)