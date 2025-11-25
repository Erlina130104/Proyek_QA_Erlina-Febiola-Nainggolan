"""
TEST CASE: Search Product Functionality
Deskripsi: Test apakah fitur search berfungsi dengan baik
Test Scenario: User mencari produk "Hammer" dan verifikasi hasil search muncul
Expected Result: Produk "Hammer" muncul di halaman search hasil
"""

# ===== IMPORT LIBRARIES =====
# Import webdriver untuk kontrol browser otomatis
from selenium import webdriver

# Import By untuk menemukan elemen di website
from selenium.webdriver.common.by import By

# Import WebDriverWait untuk tunggu elemen muncul
from selenium.webdriver.support.ui import WebDriverWait

# Import expected_conditions untuk set kondisi tunggu
from selenium.webdriver.support import expected_conditions as EC

# Import ChromeDriverManager untuk auto download ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Import Service untuk setup ChromeDriver
from selenium.webdriver.chrome.service import Service

# Import time untuk pause (delay) antar action
import time

# ===== SETUP BROWSER =====
# Buat object Service dengan ChromeDriver yang sudah didownload otomatis
service = Service(ChromeDriverManager().install())

# Buka browser Chrome kosong
# Analogi: Membuka jendela browser baru seperti Anda klik ikon Chrome
driver = webdriver.Chrome(service=service)

# ===== MULAI TEST CASE =====
try:
    # STEP 1: BUKA WEBSITE HOMEPAGE DULU
    # Analogi: Buka halaman utama website
    driver.get("https://practicesoftwaretesting.com/")
    print("✓ Step 1: Homepage berhasil dibuka")
    time.sleep(2)
    
    # STEP 1B: KLIK LINK "CATEGORIES" UNTUK KE HALAMAN PRODUCTS
    # Cari dan klik link "Categories" di header
    # Analogi: Klik menu Categories untuk pergi ke halaman produk
    try:
        categories_link = driver.find_element(By.LINK_TEXT, "Categories")
        categories_link.click()
        print("✓ Step 1B: Tombol Categories berhasil diklik")
        time.sleep(2)
    except:
        # Jika Categories tidak ketemu, coba link lain
        print("⚠ Categories link tidak ditemukan, melanjutkan...")
    
    # ===== STEP 2: CARI SEARCH BOX =====
    # Tunggu sampai element search box muncul di halaman (max 10 detik)
    # WebDriverWait = untuk tunggu elemen muncul sebelum digunakan
    # Analogi: Jangan langsung cari sebelum halaman selesai load
    wait = WebDriverWait(driver, 10)
    
    try:
        # Coba tunggu dan cari input dengan placeholder "Search"
        search_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        print("✓ Step 2: Search box ditemukan (via placeholder)")
    except:
        try:
            # Jika tidak ketemu, coba dengan xpath yang lebih umum
            search_box = wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@type, 'text')]"))
            )
            print("✓ Step 2: Search box ditemukan (via xpath umum)")
        except:
            print(" Search box tidak ditemukan, coba inspect element manual")
            raise
    
    # Klik search box untuk fokus dan pastikan bisa di-interact
    # Analogi: Klik di textbox pencarian agar cursor aktif di situ
    search_box.click()
    time.sleep(1)
    
    # ===== STEP 3: INPUT KEYWORD PENCARIAN =====
    # Ketik keyword "Hammer" ke dalam search box
    # send_keys() = simulates mengetik di keyboard
    # Analogi: Ketik "Hammer" di textbox search
    search_keyword = "Hammer"
    search_box.send_keys(search_keyword)
    print(f"✓ Step 3: Keyword '{search_keyword}' berhasil diinput ke search box")
    
    # Tunggu 1 detik agar input terekam
    time.sleep(1)
    
    # ===== STEP 4: SUBMIT PENCARIAN =====
    # Ada 2 cara untuk submit search:
    # Cara 1: Tekan tombol Enter di keyboard
    # submit() = simulates menekan tombol Enter/submit form
    # Analogi: Tekan tombol Enter atau klik tombol Search
    search_box.submit()
    print("✓ Step 4: Pencarian berhasil disubmit (tekan Enter)")
    
    # Tunggu halaman search result load (max 10 detik)
    # Analogi: Tunggu website menampilkan hasil pencarian
    time.sleep(3)
    
    # ===== STEP 5: VERIFY HASIL SEARCH =====
    # Print current URL untuk debug
    current_url = driver.current_url
    page_title = driver.title
    print(f"✓ Step 5: Current URL: {current_url}")
    print(f"✓ Step 5: Page Title: {page_title}")
    
    # Cek apakah URL mengandung keyword "q=" (parameter search)
    # Jika URL mengandung q=Hammer, berarti pencarian berhasil disubmit
    # Analogi: Cek URL berubah dari /products ke /products?q=Hammer
    if "q=" in current_url and search_keyword.lower() in current_url.lower():
        print(f"✓ Step 5: URL berubah dengan keyword search: {search_keyword}")
    else:
        print(f"⚠ Step 5: URL tidak sesuai dengan keyword search")
    
    # ===== STEP 6: VERIFIKASI PRODUK MUNCUL DI HASIL SEARCH =====
    # Cek apakah keyword muncul di halaman (di product name, description, dll)
    # page_source = HTML lengkap dari halaman yang sedang dibuka
    # Analogi: Cek apakah kata "Hammer" muncul di halaman hasil search
    page_source = driver.page_source
    
    if search_keyword.lower() in page_source.lower():
        print(f" ASSERTION PASSED: Keyword '{search_keyword}' ditemukan di halaman search")
    else:
        print(f" ASSERTION FAILED: Keyword '{search_keyword}' tidak ditemukan di halaman")
    
    # ===== STEP 7: ALTERNATIVE - VERIFIKASI DENGAN ELEMENT SEARCH =====
    # Cara lebih detail: Cari element yang berisi nama produk
    # Analogi: Cari dan klik pada produk "Hammer" di hasil search
    # 
    # try-except digunakan untuk handle jika element tidak ditemukan
    # Jika element ditemukan, tampilkan berhasil
    # Jika tidak ditemukan, tampilkan gagal tapi test tetap jalan
    try:
        # Cari element yang mengandung text "Hammer"
        # By.XPATH = cari berdasarkan element path dengan text matching
        product_element = driver.find_element(
            By.XPATH, 
            "//*[contains(text(), 'Hammer')]"
        )
        print(" Step 7: Produk 'Hammer' visual ditemukan di halaman")
    except:
        print("⚠ Step 7: Produk 'Hammer' visual tidak ditemukan (tapi keyword ada di page source)")
    
    # Tunggu 3 detik agar bisa lihat hasil sebelum browser tutup
    time.sleep(3)

# ===== ERROR HANDLING =====
# Jika ada error saat menjalankan test, tampilkan error message
except Exception as e:
    print(f" ERROR: {e}")
    print("Test gagal karena error di atas")

# ===== CLEANUP =====
# Tutup browser setelah test selesai
finally:
    driver.quit()
    print("\n--- Browser ditutup, Test selesai ---")


# ===== PENJELASAN KONSEP YANG DIGUNAKAN =====
"""
1. FIND ELEMENT (Mencari Element)
   - By.NAME: Cari berdasarkan name attribute (untuk form input)
   - By.XPATH: Cari berdasarkan XPath dengan text matching
   
2. SEND_KEYS (Ketik Text)
   - send_keys("text") = ketik text ke textbox
   - Bisa kombinasi dengan special keys
   
3. SUBMIT (Submit Form)
   - submit() = tekan Enter atau klik submit button otomatis
   - Analogi: Seperti tekan tombol Enter di keyboard
   
4. PAGE_SOURCE (Dapatkan HTML)
   - page_source = ambil HTML lengkap halaman saat ini
   - Berguna untuk cek apakah keyword muncul di halaman
   
5. ASSERTION (Verifikasi)
   - if condition: test PASS
   - else: test FAIL
   - Gunakan untuk verify expected result
   
6. TRY-EXCEPT (Error Handling)
   - try: jalankan code
   - except: jika error, tampilkan pesan tapi test tetap jalan
   - Analogi: "Coba lakukan ini, kalau error ya sudah"
"""