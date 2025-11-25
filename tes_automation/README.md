# Test Automation - Selenium

Folder ini berisi script test automation yang dibuat menggunakan Selenium untuk melakukan automated testing.

## Overview

Saya telah membuat 4 script automation untuk menguji fitur-fitur utama dari website e-commerce:
1. Test Login
2. Test Product Search
3. Test Product Filtering
4. Test Add to Cart

## Prerequisites
Python 3.7+
Selenium WebDriver
ChromeDriver atau Firefox WebDriver

## Setup

1. Install dependencies:
pip install selenium

2. Download WebDriver:
   - Chrome: https://chromedriver.chromium.org/
   - Firefox: https://github.com/mozilla/geckodriver/releases

3. Letakkan WebDriver di folder yang sama dengan script atau tambahkan ke PATH

## Script Automation

### 1. Test Login (test_login.py)

**Purpose:** Test fitur login dengan berbagai skenario

**Test Cases:**
- Login dengan email dan password valid
- Login dengan password salah
- Login dengan email tidak terdaftar
- Login dengan field kosong

**How to Run:**
python test_login.py

**Expected Result:**
Semua test case PASS, user berhasil login atau error message muncul sesuai scenario

### 2. Test Product Search (test_search.py)

**Purpose:** Test fitur pencarian produk

**Test Cases:**
- Search produk dengan keyword yang ada
- Search produk dengan keyword yang tidak ada
- Search dengan special characters
- Search dengan field kosong

**How to Run:**
python test_search.py

**Expected Result:**
Search berhasil menampilkan produk yang sesuai atau pesan "No results found"

### 3. Test Product Filtering (test_filter.py)

**Purpose:** Test fitur filter produk

**Test Cases:**
- Filter berdasarkan kategori
- Filter berdasarkan brand
- Filter berdasarkan price range
- Kombinasi multiple filter

**How to Run:**
python test_filter.py

**Expected Result:**
Produk ter-filter sesuai dengan kriteria yang dipilih

### 4. Test Add to Cart (test_add_to_cart.py)

**Purpose:** Test fitur menambahkan produk ke cart

**Test Cases:**
- Add to cart dengan quantity valid
- Add to cart dengan quantity 0
- Add to cart multiple products
- Verifikasi total cart

**How to Run:**
python test_add_to_cart.py

**Expected Result:**
Produk berhasil ditambahkan ke cart dan total terupdate dengan benar

## Run All Tests
pytest test_*.py

## Test Results

Total Scripts: 4
PASS: 4 (100%)
FAIL: 0 (0%)

## Important Notes

- Pastikan website bisa diakses sebelum menjalankan automation
- Selenium akan membuka browser secara otomatis
- Jangan close browser saat test sedang berjalan
- Screenshot akan tersimpan di folder jika ada failure

## Troubleshooting

**WebDriver not found:**
- Pastikan WebDriver ada di PATH atau di folder yang sama dengan script

**Element not found:**
- Website mungkin loading lambat, tambahkan wait time

**Connection refused:**
- Pastikan website bisa diakses