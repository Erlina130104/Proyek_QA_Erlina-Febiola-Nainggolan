# Test Case Documentation

Folder ini berisi file Excel lengkap dengan 142 test case yang saya buat untuk website e-commerce (practicesoftwaretesting.com).

## Daftar File

- `Test_Case_Erlina Febiola Nainggolan.xlsx` - File lengkap dengan semua 142 test case

## Struktur Test Case

Setiap test case di-dokumentasikan dengan struktur berikut:

- **Test Case ID** - Identitas unik untuk setiap test case (contoh: REG-001, LGN-002)
- **Test Scenario** - Deskripsi singkat apa yang akan ditest
- **Severity** - Tingkat kepentingan (Critical, High, Medium, Low)
- **Type** - Jenis test (Functional, Validation, Negative, dll)
- **Pre-condition** - Kondisi awal sebelum test dijalankan
- **Steps** - Langkah-langkah yang harus dilakukan
- **Test Data** - Data yang digunakan untuk test
- **Expected Result** - Hasil yang seharusnya terjadi
- **Actual Result** - Hasil yang terjadi saat test dijalankan
- **Status** - PASS atau FAIL
- **Notes** - Catatan tambahan atau bug yang ditemukan

## Kategori Test Case

1. **Customer Registration (REG-001 s/d REG-011)** - 11 test case
   Testing fitur registrasi pengguna baru

2. **Login (LGN-001 s/d LGN-014)** - 14 test case
   Testing fitur login dengan berbagai skenario

3. **My Account (TC_MA_001 s/d TC_MA_012)** - 12 test case
   Testing halaman akun pengguna

4. **Home Product Catalog (HOME-001 s/d HOME-011)** - 11 test case
   Testing katalog produk di halaman utama

5. **Categories - Hand Tools (CAT-HT-001 s/d CAT-HT-013)** - 13 test case
   Testing kategori hand tools

6. **Categories - Power Tools (CAT-PT-001 s/d CAT-PT-018)** - 18 test case
   Testing kategori power tools

7. **Categories - Special Tools (CAT-ST-001 s/d CAT-ST-005)** - 5 test case
   Testing kategori special tools

8. **Categories - Rentals (CAT-RNT-001 s/d CAT-RNT-003)** - 3 test case
   Testing kategori rental

9. **Product Detail Page (PDP-001 s/d PDP-010)** - 10 test case
   Testing halaman detail produk

10. **Contact Form (CNT-001 s/d CNT-011)** - 10 test case
    Testing form kontak

11. **Security Testing (SEC-001 s/d SEC-015)** - 15 test case
    Testing keamanan sistem

## Hasil Testing

- **Total Test Case:** 142
- **PASS:** 135 (95%)
- **FAIL:** 4 (3%)
- **BLOCKED:** 3 (2%)

## Bug yang Ditemukan

Dari 142 test case, ada 4 test case yang gagal karena bug:

1. **Password Validation Error** - Error message tidak akurat
2. **XSS di Search Feature** - Script berbahaya bisa dijalankan
3. **Brute Force Vulnerability** - Tidak ada pembatasan login attempt
4. **Misleading Error Message** - Error message membingungkan user

## Cara Menggunakan File Ini

1. Buka file Excel
2. Lihat sheet yang sesuai dengan kategori test
3. Ikuti langkah-langkah yang ada di kolom "Steps"
4. Dokumentasikan hasil testing di kolom "Actual Result"
5. Tandai status PASS atau FAIL