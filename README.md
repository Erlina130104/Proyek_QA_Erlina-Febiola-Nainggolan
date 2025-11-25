# Portfolio QA Tester - Erlina Febiola Nainggolan

Halo, saya Erlina Febiola Nainggolan, seorang QA Tester dengan pengalaman dalam melakukan testing aplikasi web dan API. Di repository ini saya dokumentasikan semua pekerjaan testing yang sudah saya lakukan.

## Tentang Portfolio Ini

Portfolio ini berisi dokumentasi lengkap dari testing yang saya lakukan pada sebuah website e-commerce (practicesoftwaretesting.com). Termasuk manual testing, API testing, test automation, dan security testing.

Total test case yang saya buat dan jalankan adalah 142 test case dengan pass rate 95%, dan saya berhasil menemukan 3 security vulnerabilities.

## Struktur Folder

### Excel_Tes_Case
Folder ini berisi file Excel dengan 142 test case yang sudah saya dokumentasikan. Test case mencakup:
- Customer Registration (11 test case)
- User Login (14 test case)
- My Account Management (12 test case)
- Product Catalog (11 test case)
- Product Categories (33 test case)
- Product Detail Page (10 test case)
- Contact Form (10 test case)
- Security Testing (15 test case)

Setiap test case memiliki dokumentasi lengkap dengan expected result, actual result, dan status (pass/fail).

### Manual_Testing
Folder ini berisi dokumentasi dari test case yang sudah dijalankan secara manual. Termasuk screenshot hasil testing, bug report, dan security findings.

### tes_api
Di folder ini saya dokumentasikan API testing yang dilakukan menggunakan Postman. Testing mencakup:
- Login endpoint (POST)
- Get Products endpoint (GET)
- Add to Cart endpoint (POST)
- User Profile endpoint (GET)
- Negative test cases

Hasil testing menunjukkan semua endpoint berjalan dengan baik, meskipun ditemukan beberapa vulnerability yang perlu diperbaiki.

### tes_automation
Folder ini berisi script test automation yang saya buat menggunakan Selenium. Ada 4 script automation yang sudah saya buat:
- Login automation
- Product search automation
- Product filtering automation
- Add to cart automation

## Hasil Testing

**Total Test Cases:** 142
**Status PASS:** 135 (95%)
**Status FAIL:** 4 (2%)
**Tidak Dijalankan:** 3 (3%)

**Bug & Vulnerability yang Ditemukan:**
1. XSS vulnerability di fitur search
2. Tidak ada pembatasan percobaan login (rentan brute force)
3. Stored XSS pada form registrasi
4. Error message yang membingungkan di contact form

## Tools yang Digunakan

- **Postman** - untuk API testing dan dokumentasi
- **Selenium** - untuk test automation
- **Browser DevTools** - untuk debugging dan inspection
- **Excel** - untuk dokumentasi test case

## Keahlian yang Ditunjukkan

- Manual Testing (Functional, UI/UX, Security)
- API Testing
- Test Automation menggunakan Selenium
- Security Testing (XSS, SQL Injection, CSRF)
- Test Case Documentation
- Bug Reporting dan Severity Classification
- Regression Testing
- Negative Testing

## Kontak

Email: erlinanainggolan130104@gmail.com
LinkedIn: https://www.linkedin.com/in/erlina-febiola-nainggolan-293b11368/?trk=opento_sprofile_details
GitHub: github.com/Erlina130104

---

Terima kasih telah melihat portfolio saya. Semoga ini dapat memberikan gambaran tentang kemampuan saya dalam bidang Quality Assurance dan Testing.