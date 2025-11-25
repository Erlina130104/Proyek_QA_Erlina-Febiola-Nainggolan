# Manual Testing Documentation

Folder ini berisi dokumentasi lengkap dari manual testing yang dilakukan terhadap website e-commerce (practicesoftwaretesting.com).

## Overview

Saya telah melakukan manual testing komprehensif terhadap aplikasi web e-commerce dengan fokus pada:
- Functional testing
- UI/UX testing
- Negative testing
- Security testing

## Apa yang Ditest

### 1. Registrasi Pengguna
Testing fitur registrasi dengan berbagai skenario:
- Registrasi dengan data valid
- Registrasi dengan field kosong
- Validasi format email
- Validasi kekuatan password
- Pesan error yang jelas

### 2. Login Pengguna
Testing fitur login dengan:
- Email dan password valid
- Email tidak terdaftar
- Password salah
- Field kosong
- Format email invalid

### 3. Manajemen Profil
Testing fitur di halaman My Account:
- Navigasi menu
- Edit profile
- Lihat favorites
- Lihat invoices
- Lihat messages

### 4. Katalog Produk
Testing fitur pencarian dan filter:
- Search produk berdasarkan keyword
- Filter berdasarkan kategori
- Filter berdasarkan brand
- Filter berdasarkan price range
- Sort berdasarkan harga, nama, CO2
- Pagination

### 5. Detail Produk
Testing halaman detail produk:
- Tampilan informasi produk
- Gambar produk
- Harga
- Add to cart functionality
- Add to favorites
- Related products

### 6. Security Testing
Testing keamanan aplikasi:
- SQL Injection di login
- SQL Injection di search
- XSS di form
- Session management
- CSRF protection

## Tools yang Digunakan

- Browser (Chrome/Firefox) untuk testing
- Browser DevTools untuk debugging
- Postman untuk API testing
- Screenshot tools untuk dokumentasi

## Bug yang Ditemukan

### 1. XSS Vulnerability di Search
**Severity:** High
**Location:** Search bar
**How to Reproduce:** Masukkan `<script>alert('XSS')</script>` di search
**Impact:** Script berbahaya bisa dijalankan

### 2. No Login Attempt Limit
**Severity:** High
**Location:** Login page
**Impact:** Rentan terhadap brute force attack

### 3. Stored XSS di Registration
**Severity:** High
**Location:** Registration form
**Impact:** Data malicious bisa disimpan

### 4. Misleading Error Message
**Severity:** Medium
**Location:** Contact form
**Impact:** User confusion saat ada error

## Test Results Summary

- Total Test Case: 142
- PASS: 135 (95%)
- FAIL: 4 (3%)
- BLOCKED: 3 (2%)

## Catatan Penting

Semua testing dilakukan secara manual tanpa automated tools, kecuali untuk API testing yang menggunakan Postman.

Setiap bug yang ditemukan sudah didokumentasikan dengan detail reproduction steps, severity level, dan expected fix.