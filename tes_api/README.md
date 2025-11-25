# API Testing Documentation

Folder ini berisi dokumentasi API testing yang dilakukan menggunakan Postman terhadap website e-commerce.

## Base URL

https://api.practicesoftwaretesting.com

## Endpoint yang Ditest

### 1. POST /login
**Purpose:** Login pengguna dan mendapatkan authentication token

**Request:**
Method: POST
Body:
{
"email": "user@example.com",
"password": "password123"
}

**Expected Response:**
Status: 200
Body:
{
"token": "eyJhbGc...",
"user_id": 123
}

**Test Case:**
- Login dengan email dan password valid
- Login dengan password salah
- Login dengan email tidak terdaftar
- Login tanpa mengisi field

### 2. GET /products
**Purpose:** Mendapatkan daftar produk

**Query Parameters:**
- `search` - Cari produk berdasarkan keyword
- `category` - Filter berdasarkan kategori
- `limit` - Jumlah produk per halaman
- `offset` - Pagination offset

**Expected Response:**
Status: 200
Body:
[
{
"id": 1,
"name": "Product Name",
"price": 99.99,
"category": "tools"
}
]

**Test Case:**
- Get semua produk
- Search produk dengan keyword valid
- Search dengan keyword tidak ada
- Filter kategori
- Pagination

### 3. GET /products/:id
**Purpose:** Mendapatkan detail produk berdasarkan ID

**Path Parameters:**
- `id` - Product ID

**Expected Response:**
Status: 200
Body:
{
"id": 1,
"name": "Product Name",
"price": 99.99,
"description": "...",
"image": "url",
"stock": 10
}

**Test Case:**
- Get product dengan ID valid
- Get product dengan ID tidak ada
- Get product dengan ID format invalid

### 4. POST /cart
**Purpose:** Menambahkan produk ke cart

**Headers:**
Authorization: Bearer {token}

**Request:**
Method: POST
Body:
{
"product_id": 1,
"quantity": 2
}

**Expected Response:**
Status: 201
Body:
{
"cart_id": 123,
"product_id": 1,
"quantity": 2,
"total": 199.98
}

**Test Case:**
- Add to cart dengan quantity valid
- Add to cart dengan quantity 0
- Add to cart dengan product ID invalid
- Add to cart tanpa token (unauthorized)

### 5. GET /user/profile
**Purpose:** Mendapatkan profil pengguna

**Headers:**
Authorization: Bearer {token}

**Expected Response:**
Status: 200
Body:
{
"id": 123,
"name": "Erlina",
"email": "erlina@example.com",
"phone": "081234567890"
}

**Test Case:**
- Get profile dengan token valid
- Get profile dengan token invalid
- Get profile tanpa token

## Test Results

Total API Endpoint: 5
Test Case: 12
PASS: 11 (92%)
FAIL: 1 (8%)

## Vulnerability Found

1. **No Login Attempt Limit** - Bisa retry login unlimited
2. **Weak Password Validation** - Password requirement tidak strict

## Tools

- Postman
- Postman Collection: `postman_collection.json`

## Cara Menggunakan

1. Import file `postman_collection.json` ke Postman
2. Set environment variable untuk base URL
3. Jalankan request satu per satu
4. Dokumentasikan response dan hasil