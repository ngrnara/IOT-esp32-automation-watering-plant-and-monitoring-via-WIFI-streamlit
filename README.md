# 🌱 Smart Plant IoT: Automation & Monitoring System

## 📚 Overview EN
A full-stack IoT solution for precision farming. This project uses an **ESP32** microcontroller to monitor soil moisture levels and automatically control a water pump when the soil gets dry. Data is logged securely to the cloud and visualized on a web dashboard.

## 🚀 Key Features
* **Auto-Watering:** Automatically activates the pump when soil moisture drops below a specific threshold.
* **Smart Logging:** Efficient data transmission (HTTPS) to Google Sheets only when status changes (Event-Based).
* **Real-time Dashboard:** Interactive monitoring via **Streamlit** (Python) displaying moisture trends, pump status, and watering duration.
* **Cloud Integration:** Uses Google Sheets as a database backend.

## 🛠️ Tech Stack
* **Hardware:** ESP32, Capacitive Soil Moisture Sensor, 5V Relay, Water Pump.
* **Firmware:** C++ (Arduino IDE) with WiFiClientSecure.
* **Backend:** Google Apps Script & Google Sheets.
* **Frontend:** Python, Streamlit, Plotly, Pandas.

## 📊 Dashboard Preview

## 📚 Overview ID

# 🌱 Smart Plant IoT: Sistem Monitoring & Irigasi Otomatis

Proyek ini adalah solusi IoT *end-to-end* untuk perawatan tanaman cerdas. Menggunakan mikrokontroler **ESP32**, alat ini membaca kelembapan tanah dan menyalakan pompa air secara otomatis saat tanah kering. Semua data tercatat di Cloud dan dapat dipantau melalui Web Dashboard.

## 🚀 Fitur Utama
* **Auto-Watering:** Pompa menyala otomatis berdasarkan ambang batas (*threshold*) sensor kelembapan.
* **Smart Logging:** Mengirim data via HTTPS ke Google Sheets dengan metode efisiensi data (hanya lapor saat status berubah/interval rutin).
* **Real-time Dashboard:** Visualisasi data menggunakan **Streamlit** (Python) untuk memantau grafik kelembapan, status pompa (ON/OFF), dan durasi penyiraman.
* **Cloud Database:** Integrasi langsung dengan Google Sheets.

## 🛠️ Teknologi yang Digunakan
* **Hardware:** ESP32, Sensor Kelembapan Kapasitif, Relay 5V, Pompa Air.
* **Firmware:** C++ (Arduino IDE) dengan protokol HTTPS.
* **Backend:** Google Apps Script & Google Sheets.
* **Frontend:** Python, Streamlit, Plotly, Pandas.

## 📊 Tampilan Dashboard
