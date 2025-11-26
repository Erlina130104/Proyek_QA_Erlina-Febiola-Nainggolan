# Database Testing Documentation

## Ringkasan

File ini berisi dokumentasi lengkap untuk database testing pada aplikasi Practice Software Testing website. Testing ini dirancang untuk memverifikasi integritas data yang tersimpan di database setelah melakukan berbagai operasi (registrasi, login, add to cart, checkout, dll).

Saat ini database testing masih dalam tahap dokumentasi dan test plan. Eksekusi aktual akan dilakukan setelah mendapatkan akses ke database application.

---

## Tujuan Database Testing

1. **Verifikasi Data Storage** - Pastikan data yang dikirim melalui API disimpan dengan benar di database
2. **Check Data Integrity** - Memastikan tidak ada data yang corrupt atau hilang
3. **Validasi Relationships** - Verifikasi foreign key dan relationship antar table
4. **Security Verification** - Pastikan sensitive data (password) di-encrypt/hash dengan proper
5. **Orphan Record Detection** - Cek apakah ada record tanpa reference yang valid

---

## Asumsi Database Schema

Berdasarkan API response yang kami test, berikut adalah asumsi struktur database:

### Table: users
Menyimpan informasi pengguna yang register

```
Columns:
- id (INT, Primary Key)
- email (VARCHAR, UNIQUE)
- password_hash (VARCHAR)
- first_name (VARCHAR)
- last_name (VARCHAR)
- phone (VARCHAR)
- address (VARCHAR)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Table: products
Menyimpan data produk

```
Columns:
- id (INT, Primary Key)
- name (VARCHAR)
- description (TEXT)
- price (DECIMAL)
- category (VARCHAR)
- stock (INT)
- image_url (VARCHAR)
- created_at (TIMESTAMP)
```

### Table: cart_items
Menyimpan item yang ada di shopping cart user

```
Columns:
- id (INT, Primary Key)
- user_id (INT, Foreign Key to users)
- product_id (INT, Foreign Key to products)
- quantity (INT)
- added_price (DECIMAL)
- created_at (TIMESTAMP)
```

### Table: orders
Menyimpan order history user

```
Columns:
- id (INT, Primary Key)
- user_id (INT, Foreign Key to users)
- total_price (DECIMAL)
- status (VARCHAR) - 'pending', 'completed', 'cancelled'
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Table: order_items
Detail item yang ada dalam satu order

```
Columns:
- id (INT, Primary Key)
- order_id (INT, Foreign Key to orders)
- product_id (INT, Foreign Key to products)
- quantity (INT)
- unit_price (DECIMAL)
- total_price (DECIMAL)
```

---

## Database Test Cases

### Test Case DB-001: Verifikasi User Registration Data

**Deskripsi:** Pastikan data user yang baru register tersimpan dengan benar di database

**Pre-condition:** User sudah berhasil register melalui UI

**Test Query:**
```sql
SELECT id, email, first_name, last_name, phone, address, created_at 
FROM users 
WHERE email = 'erlina@example.com';
```

**Data Test:**
- Email: erlina@example.com
- First Name: Erlina
- Last Name: Febiola
- Phone: 081234567890
- Address: Medan, North Sumatra

**Expected Result:**
- Record user harus ada di table users
- Email harus match: erlina@example.com
- first_name harus: Erlina
- last_name harus: Febiola
- phone harus: 081234567890
- address harus: Medan, North Sumatra
- created_at harus hari/waktu saat user register

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** HIGH
**Type:** Functional

---

### Test Case DB-002: Verifikasi Password Security

**Deskripsi:** Memastikan password di-hash/encrypt, bukan disimpan dalam plain text

**Pre-condition:** User sudah register

**Test Query:**
```sql
SELECT email, password_hash, LENGTH(password_hash) as password_length 
FROM users 
WHERE email = 'erlina@example.com';
```

**Expected Result:**
- password_hash harus ada dan tidak kosong
- password_hash harus dalam format hash/encrypted (contoh: $2y$10$... atau bcrypt format)
- password_hash harus NOT sama dengan original password
- Panjang password_hash minimal 50 karakter (tidak boleh kurang)
- Value tidak boleh readable sebagai plain text

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** CRITICAL
**Type:** Security

---

### Test Case DB-003: Verifikasi Add to Cart Data

**Deskripsi:** Memastikan product yang di-add ke cart tersimpan dengan benar di database

**Pre-condition:** User sudah login, product sudah ada di database

**Test Query:**
```sql
SELECT ci.id, ci.user_id, ci.product_id, ci.quantity, 
       p.name, p.price, ci.added_price, ci.created_at
FROM cart_items ci
JOIN products p ON ci.product_id = p.id
WHERE ci.user_id = 1 AND ci.product_id = 5;
```

**Data Test:**
- User ID: 1 (Erlina)
- Product ID: 5 (Hand Drill)
- Quantity: 2

**Expected Result:**
- Record harus ada di table cart_items
- user_id harus: 1
- product_id harus: 5
- quantity harus: 2
- product name harus: Hand Drill
- product price harus match dengan table products
- added_price harus: price × quantity
- created_at harus sesuai waktu add to cart
- Foreign key relationship harus valid (product harus ada di products table)

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** HIGH
**Type:** Functional

---

### Test Case DB-004: Deteksi Orphan Records di Cart Items

**Deskripsi:** Memastikan tidak ada orphan records (cart_items tanpa user yang valid)

**Pre-condition:** Database sudah berisi multiple cart items

**Test Query:**
```sql
SELECT ci.id, ci.user_id, ci.product_id 
FROM cart_items ci
WHERE ci.user_id NOT IN (SELECT id FROM users);
```

**Expected Result:**
- Query harus return 0 rows (tidak ada orphan data)
- Semua cart_items harus punya valid user_id yang ada di users table
- Tidak boleh ada record dengan user_id yang sudah dihapus

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** MEDIUM
**Type:** Data Integrity

---

### Test Case DB-005: Deteksi Orphan Records di Cart Items - Product

**Deskripsi:** Memastikan tidak ada cart_items dengan product_id yang tidak valid

**Pre-condition:** Database sudah berisi multiple cart items

**Test Query:**
```sql
SELECT ci.id, ci.user_id, ci.product_id 
FROM cart_items ci
WHERE ci.product_id NOT IN (SELECT id FROM products);
```

**Expected Result:**
- Query harus return 0 rows
- Semua product_id di cart_items harus valid dan ada di products table
- Jika product dihapus, cart_items yang reference product harus juga dihapus

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** MEDIUM
**Type:** Data Integrity

---

### Test Case DB-006: Verifikasi Order Data Setelah Checkout

**Deskripsi:** Memastikan order tersimpan dengan lengkap setelah user checkout

**Pre-condition:** User sudah checkout, order berhasil dibuat

**Test Query:**
```sql
SELECT o.id, o.user_id, o.total_price, o.status, o.created_at,
       COUNT(oi.id) as total_items,
       SUM(oi.total_price) as sum_items_price
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id
WHERE o.user_id = 1
GROUP BY o.id
ORDER BY o.created_at DESC LIMIT 1;
```

**Expected Result:**
- Order record harus ada di table orders
- user_id harus: 1
- total_price harus > 0
- status harus salah satu dari: 'pending', 'completed', 'cancelled'
- created_at harus sesuai waktu checkout
- total_items (COUNT order_items) harus >= 1
- sum_items_price harus match dengan order.total_price (atau close)
- Foreign key relationship valid (user harus ada di users table)

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** HIGH
**Type:** Functional

---

### Test Case DB-007: Verifikasi Order Items Detail

**Deskripsi:** Memastikan detail item dalam order tersimpan dengan benar

**Pre-condition:** Order sudah dibuat dengan multiple items

**Test Query:**
```sql
SELECT oi.id, oi.order_id, oi.product_id, oi.quantity, 
       oi.unit_price, oi.total_price, p.name, p.price
FROM order_items oi
JOIN products p ON oi.product_id = p.id
WHERE oi.order_id = 1
ORDER BY oi.id;
```

**Expected Result:**
- Setiap order_item record harus ada
- product_id harus valid (ada di products table)
- quantity harus > 0
- unit_price harus match dengan product price saat order dibuat
- total_price harus = quantity × unit_price
- Product name dan price harus valid
- Tidak ada item dengan quantity 0 atau negative

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** HIGH
**Type:** Functional

---

### Test Case DB-008: Deteksi Orphan Records di Order Items

**Deskripsi:** Memastikan tidak ada order_items tanpa order yang valid

**Pre-condition:** Database sudah berisi order items

**Test Query:**
```sql
SELECT oi.id, oi.order_id, oi.product_id
FROM order_items oi
WHERE oi.order_id NOT IN (SELECT id FROM orders);
```

**Expected Result:**
- Query harus return 0 rows
- Semua order_items harus punya valid order_id
- Tidak boleh ada orphan order items

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** MEDIUM
**Type:** Data Integrity

---

### Test Case DB-009: Verifikasi Unique Constraint pada Email

**Deskripsi:** Memastikan email unique, tidak boleh ada duplikat

**Pre-condition:** Ada user dengan email erlina@example.com

**Test Query:**
```sql
SELECT COUNT(*) as total_count, email
FROM users
WHERE email = 'erlina@example.com'
GROUP BY email;
```

**Expected Result:**
- COUNT harus = 1 (tidak boleh ada duplikat)
- Email harus unique di database
- Database harus enforce UNIQUE constraint pada email column

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** MEDIUM
**Type:** Data Integrity

---

### Test Case DB-010: Data Consistency - Total Price Verification

**Deskripsi:** Memastikan total_price di order match dengan sum dari order_items

**Pre-condition:** Order sudah selesai dengan multiple items

**Test Query:**
```sql
SELECT o.id, o.total_price,
       SUM(oi.total_price) as calculated_total,
       CASE 
           WHEN o.total_price = SUM(oi.total_price) THEN 'MATCH'
           ELSE 'MISMATCH'
       END as consistency_check
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id
WHERE o.id = 1
GROUP BY o.id;
```

**Expected Result:**
- o.total_price harus = SUM(oi.total_price)
- consistency_check harus: 'MATCH'
- Tidak boleh ada perbedaan atau rounding error yang signifikan

**Actual Result:** 
(Akan diisi saat testing dilakukan)

**Status:** READY FOR TESTING
**Severity:** HIGH
**Type:** Data Integrity

---

## Ringkasan Test Cases

| No | Test Case ID | Deskripsi | Severity | Type | Status |
|----|--------------|-----------|----------|------|--------|
| 1 | DB-001 | Verifikasi User Registration | HIGH | Functional | READY |
| 2 | DB-002 | Password Security | CRITICAL | Security | READY |
| 3 | DB-003 | Add to Cart Data | HIGH | Functional | READY |
| 4 | DB-004 | Orphan Records - Cart User | MEDIUM | Data Integrity | READY |
| 5 | DB-005 | Orphan Records - Cart Product | MEDIUM | Data Integrity | READY |
| 6 | DB-006 | Order Data | HIGH | Functional | READY |
| 7 | DB-007 | Order Items Detail | HIGH | Functional | READY |
| 8 | DB-008 | Orphan Records - Order Items | MEDIUM | Data Integrity | READY |
| 9 | DB-009 | Email Unique Constraint | MEDIUM | Data Integrity | READY |
| 10 | DB-010 | Data Consistency - Price | HIGH | Data Integrity | READY |

**Total Test Cases:** 10
**READY FOR TESTING:** 10
**PASS:** -
**FAIL:** -

---

## Tools & Environment

**Tools yang Diperlukan:**
- MySQL Workbench atau database client lainnya (DBeaver, HeidiSQL)
- Akses ke database server (development atau production)
- Database credentials (username, password, host)

**Environment:**
- Database: Practice Software Testing
- Jenis Database: MySQL (assumed)
- Waktu Eksekusi: Setelah database tersedia dan accessible

---

## Catatan & Observasi

### Findings Potential
Berdasarkan testing API yang sudah dilakukan, area-area yang perlu special attention pada database testing:

1. **Password Security** - Verifikasi bahwa password di-hash dengan algorithm yang aman (bcrypt, argon2)
2. **Foreign Key Constraints** - Pastikan semua foreign keys di-implement dan enforce
3. **Data Type Validation** - Verify bahwa semua data tersimpan dengan tipe data yang correct
4. **Null Values** - Check apakah required fields tidak boleh NULL
5. **Decimal Precision** - Untuk price fields, check precision dan rounding

---

## Kesimpulan

Database testing documentation ini sudah lengkap dan ready untuk dijalankan. Setiap test case memiliki query yang clear, expected result yang terukur, dan dapat di-execute secara independent.

Saat mendapatkan akses ke database, semua test case di atas dapat langsung dijalankan untuk memverifikasi integritas dan consistency data dalam aplikasi Practice Software Testing.

---

**Document Version:** 1.0
**Last Updated:** November 2025
**Author:** Erlina Febiola Nainggolan
**Status:** READY FOR TESTING